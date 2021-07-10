from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, mixins, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from notifications.sms_utils import send_sms
from notifications.email_utils import send_email
from .serializer import UserSerializer
from .models import User, Verification
from rest_framework.viewsets import ViewSet
from django.contrib.auth.password_validation import (
    UserAttributeSimilarityValidator,
    CommonPasswordValidator,
    MinimumLengthValidator,
    NumericPasswordValidator,
)


class UserAPIView(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        queryset = User.objects.filter(id=user.id)
        if user.is_superuser:
            queryset = User.objects.all()
        return queryset

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.destroy(request, *args, **kwargs)


class AuthenticationViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=["post"], url_path="create-user", name="create-user")
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "first_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="First name"
                ),
                "last_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Last name"
                ),
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING, description="username"
                ),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email"),
                "phone_number": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Phone number"
                ),
                "gender": openapi.Schema(
                    type=openapi.TYPE_STRING, description="gender"
                ),
                "date_of_birth": openapi.Schema(
                    type=openapi.TYPE_STRING, description="date of birth"
                ),
                "bank_name": openapi.Schema(
                    type=openapi.TYPE_STRING, description="bank name"
                ),
                "account_number": openapi.Schema(
                    type=openapi.TYPE_STRING, description="account number"
                ),
                "role": openapi.Schema(type=openapi.TYPE_STRING, description="role"),
                "country": openapi.Schema(
                    type=openapi.TYPE_STRING, description="country"
                ),
                "state": openapi.Schema(type=openapi.TYPE_STRING, description="state"),
                "address": openapi.Schema(
                    type=openapi.TYPE_STRING, description="address"
                ),
            },
            required=["first_name", "last_name", "phone_number", "account_number"],
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Account created",
                examples={
                    "application/json": {
                        "detail": "Your account has been created. Verify your email to continue"
                    }
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Account/verification code exception",
                examples={"application/json": {"detail": "Bad request"}},
            ),
        },
    )
    def create_user(self, request):
        data = request.data
        data["gender"] = data.get("gender").upper()
        data["role"] = data.get("role").upper()
        data["state"] = data.get("state").upper()
        context = {"request": request}
        serializer = UserSerializer(data=data, context=context)
        if serializer.is_valid():
            user = serializer.save()
            verification = Verification(user=user)
            verification.save()
            """
            send verification.code to user email
            """
            email = request.data.get("email")
            message = (
                "Welcome to FarmvestNG! Before you continue, activate your account by providing the verification. \n "
                "Your verification code is {code}. It expires in 5 minutes.".format(
                    code=verification.code
                )
            )
            subject = "Welcome to FarmvestNG"
            send_email(email=email, message=message, subject=subject)

            return Response(
                {"detail": "user created successfully, Verify your email"}, status=201
            )

        return Response({"detail": serializer.errors}, status=400)

    @action(detail=False, methods=["post"], url_path="verify-otp", name="verify-otp")
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "otp": openapi.Schema(type=openapi.TYPE_STRING, description="otp"),
                "phone_number": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Phone number"
                ),
            },
            required=["phone_number", "otp"],
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Verification code has been verified",
                examples={
                    "application/json": {
                        "detail": "Verification is approved. Please continue to set your password"
                    }
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Account/verification code exception",
                examples={"application/json": {"detail": "Invalid verification code"}},
            ),
        },
    )
    def verify_otp(self, request):
        otp = request.data.get("otp")
        phone_number = request.data.get("phone_number")
        user = User.objects.filter(phone_number=phone_number).first()
        verification = Verification.objects.filter(
            code=otp, is_used=False, is_valid=True
        ).first()

        if not user or not verification:
            return Response({"detail": "Invalid user or / and otp"}, status=400)
        verification.is_used = True
        verification.save()
        return Response(
            {"detail": "Verification is approved, Please continue to set your password"}
        )

    @action(
        detail=False, methods=["post"], url_path="set-password", name="set-password"
    )
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "otp": openapi.Schema(type=openapi.TYPE_STRING, description="otp"),
                "phone_number": openapi.Schema(
                    type=openapi.TYPE_STRING, description="Phone number"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="password"
                ),
            },
            required=["phone_number", "otp", "password"],
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Password created successful",
                examples={
                    "application/json": {
                        "detail": "Password created successful. Please continue to log in"
                    }
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Invalid user or / and otp",
                examples={"application/json": {"detail": "Invalid user or / and otp"}},
            ),
        },
    )
    def set_password(self, request):
        raw_password = request.data.get("password")
        phone_number = request.data.get("phone_number")
        otp = request.data.get("otp")

        password_validators = [
            UserAttributeSimilarityValidator,
            CommonPasswordValidator,
            MinimumLengthValidator,
            NumericPasswordValidator,
        ]

        try:
            for validator in password_validators:
                validator().validate(raw_password)
        except ValidationError as e:
            messages.error(request, str(e))
            return Response({"detail": e}, status=400)

        verification = Verification.objects.filter(
            code=otp, is_used=True, is_valid=True
        ).first()
        user = User.objects.filter(phone_number=phone_number).first()

        if not verification or not user:
            return Response({"detail": "Invalid user or / and otp"}, status=400)
        user.set_password(raw_password)
        user.save()
        verification.is_valid = False
        verification.save()
        return Response({"detail": "Password created successful"}, status=200)

    @action(detail=False, methods=["post"], url_path="signin", name="signin")
    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(
                    type=openapi.TYPE_STRING, description="username"
                ),
                "password": openapi.Schema(
                    type=openapi.TYPE_STRING, description="password"
                ),
            },
            required=["username", "password"],
        ),
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Logged in successfully",
                examples={
                    "application/json": {
                        "id": 18,
                        "first_name": "string",
                        "last_name": "string",
                        "username": "string",
                        "email": "user@example.com",
                        "phone_number": "string",
                        "gender": "MALE",
                        "date_of_birth": "2000-01-01",
                        "role": "INVESTOR",
                        "bank_name": "string",
                        "account_number": "string",
                        "country": "string",
                        "state": "string",
                        "address": "3453",
                        "token": "a977cb3b6794342b210d8d090407cfa881294000",
                    }
                },
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Log in errors",
                examples={"application/json": {"detail": "Invalid credentials"}},
            ),
        },
    )
    def signin(self, request):
        if not request.user.is_anonymous:
            return Response(
                {"detail": "You are not allowed to perform this action"}, status=403
            )
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password, request=request)

        if not user:
            return Response({"detail": "Invalid credentials"}, status=400)
        login(request=request, user=user)
        context = {"request": request}
        data = UserSerializer(user, context=context).data
        token, created = Token.objects.get_or_create(user=user)
        data["token"] = token.key
        return Response(data=data, status=200)

    @action(detail=False, methods=["get"], url_path="signout", name="signout")
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: openapi.Response(
                description="Successfully signed out",
                examples={"application/json": {"detail": "Signed out"}},
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response(
                description="Log out errors",
                examples={
                    "application/json": {
                        "detail": "you are not allowed to perform this action"
                    }
                },
            ),
        }
    )
    def signout(self, request):
        if request.user.is_anonymous:
            return Response(
                {"detail": "you are not allowed to perform this action"}, status=403
            )
        Token.objects.filter(user=request.user).delete()
        logout(request)
        return Response({"detail": "logged out successfully"})


# class UserPostView(generics.CreateAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserGetDetailView(generics.RetrieveAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserUpdateView(generics.RetrieveUpdateAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     # def get_object(self):
#     #     pk = self.kwargs['id']
#     # return get_object_or_404(User, id=id)
#
#
# class AllUser(generics.ListAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     # paginate_by =None
#
#
# class DeleteUserView(generics.DestroyAPIView):
#
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
