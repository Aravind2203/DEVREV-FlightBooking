# DevRev Flight Booking Management System

Welcome to the Flight Booking Management System! This system allows users to book flights, manage reservations, and perform various actions related to flight bookings. This application uses python's Django web framework as it's core backend technology and uses bootstrap library for styling the frontend

## Deployment

The application is deployed on pythonanwhere cloud server.
1. Admin url:
    [Admin-app](http://aravind2203.pythonanywhere.com/manage/flight/home)
```
    Email: aravind@gmail.com
    Password: 123 
```
2. Normal user url:
    [User-app](http://aravind2203.pythonanywhere.com/)
```
    Email: normal@gmail.com
    Password: 1234567890
```
## Tasks Completed
### User
- [X] Login
- [X] SignUp
- [X] Searching for flights with date and time
- [x] Booking tickets on fights
- [x] My booking -> list the booking made by the user
- [X] Logout

### Admin
- [X] Login
- [X] Add Flights
- [X] Remove Flights
- [X] View All booking

### Addition tasks Done
- [X] Generate PDF booking details for users


## Features

- User registration and authentication
- Search and browse available flights
- Book flights and manage reservations
- Generate PDF Invoices
- Admin dashboard for flight management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aravind2203/DEVREV-FlightBooking
   cd DEVREV-FlightBooking
   
   ```
2. Activate Virtual Environment and Install dependencies

    ```bash
    python -m venv env 
    env\Scripts\activate
    pip install -r requirements.txt
    ```
3. Run migrations

    ```bash
    python manage.py migrate
    ```
4. Run Application

    ```bash
    python manage.py runserver
    ```

5. Visit localhost:8000 in your browser

![FlighBooking App](https://github.com/Aravind2203/DEVREV-FlightBooking/assets/71716685/6fe46c23-c985-4834-95a0-9be472d0a139)
