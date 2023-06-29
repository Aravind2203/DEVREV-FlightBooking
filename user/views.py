from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bookings,Travel,Airports,Passengers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

User=get_user_model()
def home(request):
    airports=Airports.objects.all()
    return render(request,"home.html",context={"airports":airports})

def searchFlights(request):
    if request.method=="POST":
        
        source=request.POST.get("source",None)
        destination=request.POST.get("destination",None)
        if source==destination:
            messages.info(request,"Source and destination can't be same")
            return redirect("home")
        date=request.POST.get("date",None)
        source_name=Airports.objects.get(id=source)
        destination_name=Airports.objects.get(id=destination)
        travels=Travel.objects.filter(date=date,flight_id__source__id=source,flight_id__destination__id=destination,remain__gt=0)
        
        total_tavels=len(travels)

        return render(request,"search.html",context={"flights":travels,"total":total_tavels,"source_name":source_name,"destination_name":destination_name,"date":date})



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
    print(total_booking)
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
    passengers=booking.passengers_names.all()
    return render(request,"booking-detail.html",context={"booking":booking,"passengers":passengers})
    

@login_required(login_url="/login")
@csrf_exempt
def book_flight(request,id):
    try:
        travel=Travel.objects.get(id=id)
    except:
        raise ValueError("Invalid travel id given")
    if request.method=="POST":
        count=request.POST.get('count')
        if int(count)>travel.remain:
            messages.info(request,"Not enough seats.")
            return redirect("book",id=id)
        passengers=[]
        for i in range(int(count)):
            name=request.POST.get(f'name-{i+1}')
            age=request.POST.get(f'age-{i+1}')
            p=Passengers.objects.create(name=name,age=int(age))
            passengers.append(p)
        b=Bookings(user_id=request.user,travel=travel,passengers_count=int(count))
        b.save()
        b.passengers_names.set(passengers)
        travel.remain-=int(count)
        travel.save()
        messages.info(request,"Booked Successfully")
        
    return render(request,"book.html",context={"travel":travel})