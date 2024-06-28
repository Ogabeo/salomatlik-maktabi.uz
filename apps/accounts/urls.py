from django.urls import path
from apps.accounts.views import UserRegisterView, LoginView, LogOutView, UpdateUserView

app_name='accounts'
urlpatterns = [
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('update/', UpdateUserView.as_view(), name='update'),
    ]
