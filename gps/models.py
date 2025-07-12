from django.db import models

# Create your models here.


class WifiScan(models.Model):
    bssid = models.CharField(max_length=50, null=True, blank=True)
    essid = models.CharField(max_length=100, null=True, blank=True)
    power = models.IntegerField(null=True, blank=True)
    beacons = models.IntegerField(null=True, blank=True)
    first = models.CharField(max_length=50, null=True, blank=True)
    last = models.CharField(max_length=50, null=True, blank=True)
    channel = models.IntegerField(null=True, blank=True)
    speed = models.CharField(max_length=50, null=True, blank=True)
    privacy = models.CharField(max_length=50, null=True, blank=True)
    cipher = models.CharField(max_length=50, null=True, blank=True)
    auth = models.CharField(max_length=50, null=True, blank=True)
    iv = models.IntegerField(null=True, blank=True)
    ip = models.CharField(max_length=50, default="0.0.0.0", null=True, blank=True)
    idlen = models.IntegerField(null=True, blank=True)
    key = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.essid if self.essid else "Unknown"


    
class Location(models.Model):
    location_name = models.CharField(max_length=255,null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='photos/',null=True, blank=True)
    audio = models.FileField(upload_to='recordings/',null=True, blank=True)
    
    def __str__(self):
        return self.location_name if self.location_name else "Unknown Location"



class LocationWithLatLong(Location):
    pkey = models.AutoField(primary_key=True)
    mac = models.CharField(max_length=50, null=True, blank=True)
    ssid = models.CharField(max_length=100, null=True, blank=True)
    signal = models.IntegerField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    longi = models.FloatField(null=True, blank=True)
    accuracy = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    