from django.urls import path
from .views import *
urlpatterns=[
    path("login-admin",login_admin,name="login-admin"),
    path("unauthorized",unauthorized,name="unauthorized"),
    path("home",home,name="admin-home"),
    path("logout-admin",logout_admin,name="logout-admin"),
    path("airline-detail/<int:id>",airline_details,name="airline-detail"),
    path("fight-detail/<int:id>",flight_details,name="flight_detail"),
    path("travel-detail/<int:id>",travel_details,name="travel-detail"),
    path("booking-detail-admin/<int:id>",booking_details,name="booking-detail-admin"),
]