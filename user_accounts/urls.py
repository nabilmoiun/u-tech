from django.urls import path
from rest_framework.authtoken import views

from .views import (
    Login,
    RegisterUser
)

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register-user/', RegisterUser.as_view(), name='register-user'),

]
