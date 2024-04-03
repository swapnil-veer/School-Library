from django.urls import path
from .views import register_view, user_login, user_logout

urlpatterns = [
    path('register/', register_view, name='user_register'),
    path('signin/', user_login, name= "user_signin"),
    path('sign-out/', user_logout, name= "user_sign_out"),
]