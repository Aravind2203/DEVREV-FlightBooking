# DevRev Flight Booking Management System

Welcome to the Flight Booking Management System! This system allows users to book flights, manage reservations, and perform various actions related to flight bookings.

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
- View and update personal information
- View and cancel existing bookings
- Admin dashboard for flight management

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Aravind2203/DEVREV-FlightBooking
   
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