from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from rest_framework import generics, mixins
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from notifications.sms_utils import send_sms
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
    def create_user(self, request):
        data = request.data
        context = {"request": request}
        serializer = UserSerializer(data=data, context=context)
        if serializer.is_valid():
            user = serializer.save()
            verification = Verification(user=user)
            verification.save()
            """
            send verification.code to user phone number
            """
            phone = request.data.get("phone_number")
            message = "Your FarmvestNG verification code {code}".format(
                code=verification.code
            )
            recipients = [phone]
            send_sms(phone_numbers=recipients, message=message)

            return Response(
                {"detail": "user created successfully, Verify your phone number"},
                status=201,
            )

        return Response({"detail": serializer.errors}, status=400)

    @action(detail=False, methods=["post"], url_path="verify-otp", name="verify-otp")
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
        return Response({"detail": "Verification is approved"})

    @action(
        detail=False, methods=["post"], url_path="set-password", name="set-password"
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
