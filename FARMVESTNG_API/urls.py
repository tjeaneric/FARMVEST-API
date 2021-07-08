from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(  # new
    openapi.Info(
        title="FarmvestNG API",
        default_version="v1",
        description="The idea is for an app that will link local farmers to investors so they can get much needed resources to expand their production. The app will work as an intermediary between investors and farmers. The app will sort for farmers, verify them and view their profiles for investors to see. The investors will have a determined rate of return for their investment.",
        contact=openapi.Contact(email="ericjohn415@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("rest-auth/", include("rest_framework.urls")),
    # local apps
    path("api/v1/", include("User.urls")),
    path("api/v1/", include("farms.urls")),
    path("api/v1/", include("Investment.urls")),
    path("api/v1/", include("Referral.urls")),
    path(
        "documentation/",
        schema_view.with_ui("swagger", cache_timeout=0),  # new
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),  # new
        name="schema-redoc",
    ),
    path("api/v1/", include("transaction.urls")),
    path("api/v1/", include("wallet.urls")),
  
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
