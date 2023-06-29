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
    path("add-airline",add_airline,name="add-airline"),
    path("add-airport",add_airport,name="add-airport"),
    path("add-flight",add_flight,name="add-flight"),
    path("add-travel",add_travel,name="add-travel"),
    path("delete-airport/<int:id>",delete_airport,name="delete-airport"),
    path("delete-airline/<int:id>",delete_airline,name="delete-airline"),
    path("delete-flight/<int:id>",delete_flight,name="delete-flight"),
    path("delete-travel/<int:id>",delete_travel,name="delete-travel"),
]