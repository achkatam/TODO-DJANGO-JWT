from django.urls import path
from .views import UserCreate
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registration', UserCreate.as_view(), name='registration'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token_view'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh_token_view'),
]
 