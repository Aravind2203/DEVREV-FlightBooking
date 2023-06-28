from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(AirLine)
admin.site.register(Airports)
admin.site.register(Flight)
admin.site.register(Travel)
admin.site.register(Passengers)
admin.site.register(Bookings)