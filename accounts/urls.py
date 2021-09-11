from knox import views as knox_views
from .views import LoginAPI, RegisterAPI, UserAPI
from django.urls import path

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/user/', UserAPI.as_view(), name='user'),
]
