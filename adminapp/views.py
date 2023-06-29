from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,logout,authenticate
from django.contrib.auth.decorators import login_required
from user.models import AirLine,Airports,Flight,Bookings,Travel
User=get_user_model()
# Create your views here.
def login_admin(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            if user.is_superuser:
                login(request,user)
                return redirect("admin-home")
            else:
                return render(request,"adminapp/login.html",context={"error":"You are not Authorized to enter"})
        else:
            return render(request,"adminapp/login.html",context={"error":"Invalid credentials"})
    return render(request,"adminapp/login.html",context={"error":None})

def unauthorized(request):
    return render(request,"adminapp/unauthorized.html")

@login_required(login_url="/manage/flight/login-admin")
def home(request):
    if not request.user.is_superuser:
        return redirect("unauthorized")
    airlines=AirLine.objects.all()
    airports=Airports.objects.all()
    return render(request,"adminapp/home.html",context={"airlines":airlines,"airports":airports})

def logout_admin(request):
    logout(request)
    return redirect("admin-home")

@login_required(login_url="/manage/flight/login-admin")
def airline_details(request,id):
    if not request.user.is_superuser:
        return redirect("unauthorized")
    try:
        airline=AirLine.objects.get(id=id)
    except:
        raise ValueError("Invalid airline id")
    flights=Flight.objects.filter(airline=airline)
    return render(request,"adminapp/airline-detail.html",context={"airline":airline,"flights":flights})


@login_required(login_url="/manage/flight/login-admin")
def flight_details(request,id):
    if not request.user.is_superuser:
        return redirect("unauthorized")

    try:
        flight=Flight.objects.get(id=id)
    except:
        raise ValueError("Invalid flight id given")

    travels=Travel.objects.filter(flight_id=flight)
    return render(request,"adminapp/flight-detail.html",context={"flight":flight,"travels":travels})

def travel_details(request,id):
    if not request.user.is_superuser:
        return redirect("unauthorized")
    try:
        travel=Travel.objects.get(id=id)
    except:
        raise ValueError("Invalid Travel id given")
    
    bookings=Bookings.objects.filter(travel=travel)
    return render(request,"adminapp/travel-detail.html",context={"travel":travel,"bookings":bookings})

@login_required(login_url="/manage/flight/login-admin")
def booking_details(request,id):
    if not request.user.is_superuser:
        return redirect("unauthorized")
    try:
        booking=Bookings.objects.get(id=id)
    except:
        raise ValueError("Invalid booking Id")
    passengers=booking.passengers_names.all()
    return render(request,"adminapp/booking-detail.html",context={"booking":booking,"passengers":passengers})