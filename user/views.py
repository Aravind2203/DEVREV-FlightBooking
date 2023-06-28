from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bookings
# Create your views here.

User=get_user_model()
def home(request):
    return render(request,"home.html")

def searchFlights(request):
    if request.method=="POST":
        print(request.POST)
    return render(request,"home.html")

def login_user(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Logedin Successfully")
            return redirect("home")
        else:
            return render(request,"login.html",context={"error":"Invalid Credentials"})
    return render(request,"login.html",context={"error":None})

def logout_user(request):
    logout(request)
    messages.success(request,"Logedout Successfully")
    return redirect("home")

def signup_user(request):
    if request.method=="GET":
        return render(request,"signup.html")
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone_number=request.POST.get("phone_number")
        password=request.POST.get("password")
        user,created=User.objects.get_or_create(email=email)
        if created==True:
            user.name=name
            user.phone_number=phone_number
            user.set_password(password)
            user.save()
            print(user)
            messages.success(request,"User created successfully. Login to continue")
            return redirect("login")
        else:
            print(user)
            messages.info(request,"User already exists")
            return redirect("login")

@login_required(login_url="/login")
def user_profile(request):
    user=request.user
    booking=Bookings.objects.filter(user_id=user)
    total_booking=len(booking)
    data={
        "name":user.name,
        "email":user.email,
        "phone_number":user.phone_number,
        "bookings":booking,
        "total_booking":total_booking
    }
    return render(request,"profile.html",context=data)

@login_required(login_url="/login")
def booking_details(request,id):
    user=request.user
    try:
        booking=Bookings.objects.get(id=id)
    except:
        raise ValueError("Invalid booking Id")
    if user!=booking.user_id:
        return HttpResponse("<h1>You are not authorized to view this page</h1>")
    print(booking.passengers_names)
    return render(request,"booking-detail.html",context={"booking":booking})
    