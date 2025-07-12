from django.contrib import admin
from .models import WifiScan, Location

# Register your models here.
admin.site.register(WifiScan)
admin.site.register(Location)
