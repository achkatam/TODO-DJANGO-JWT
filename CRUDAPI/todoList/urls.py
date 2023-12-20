from django.urls import path
from .views import UserCreate, TodoRetrieveUpdateDestroyView, TodoListCreateView
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', TodoListCreateView.as_view(), name='list_create_view'),
    path('registration', UserCreate.as_view(), name='registration'),
    path('todo/<int:pk>', TodoRetrieveUpdateDestroyView.as_view(), name='update_delete_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='obtain_token_view'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='refresh_token_view'),
]
