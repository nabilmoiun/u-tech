from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Update Tech Test Api",
      default_version='v1',
      description="Rest apis",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="moinul.hossina.in2019@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_accounts.urls')),
    path('', include('sales.urls')), 
    path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
