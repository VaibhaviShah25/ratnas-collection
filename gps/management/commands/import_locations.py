import csv
from django.core.management.base import BaseCommand
from gps.models import WifiScan

class Command(BaseCommand):
    help = 'Import WiFi data from CSV'

    def handle(self, *args, **kwargs):
        with open('wifi_scan-01.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                WifiScan.objects.create(
                    bssid=row['BSSID'],
                    essid=row[' ESSID'],
                    power=int(row[' Power']),
                    beacons=int(row[' # beacons']),
                    #data=int(row['data']),
                    channel=int(row[' channel']),
                    #encryption=row['encryption'],
                    cipher=row[' Cipher'],
                    auth=row[' Authentication']
                )
        self.stdout.write(self.style.SUCCESS('✅ WiFi Data Imported Successfully'))
