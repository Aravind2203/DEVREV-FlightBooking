from django.urls import path
from .views import *
urlpatterns = [
    
    path('',home,name="home"),
    path("search",searchFlights,name="search"),
    path("login",login_user,name="login"),
    path("logout",logout_user,name="logout"),
    path("signup",signup_user,name="signup")
]