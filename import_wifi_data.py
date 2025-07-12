import os
import django
import pandas as pd

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject1.settings")  # Replace with your project name
django.setup()

from gps.models import WifiScan  # Replace 'myapp' with your actual app name
for i in range(1,8):
# Load CSV file
    df = pd.read_csv(f"wifi_scan-0{i}.csv", skiprows=0)  # Adjust skiprows if needed

# Drop empty rows
df = df.dropna(how='all')

# Rename columns to match Django model field names
df.columns = [
    "bssid", "first", "last", "channel", "speed", "privacy", "cipher",
    "auth", "power", "beacons", "iv", "ip", "idlen", "essid", "key"
]

# Filter only WiFi scan data (exclude "Station MAC" section)
df = df[df["bssid"].str.contains(":", na=False)]  # Keep only MAC address rows

# Convert "first" and "last" timestamps to datetime
df["first"] = pd.to_datetime(df["first"], errors='coerce')
df["last"] = pd.to_datetime(df["last"], errors='coerce')

# Replace invalid IP addresses
df["ip"] = df["ip"].str.replace(" ", "").replace("0.0.0.0", "0.0.0.0")

# Fill NaN values for integer fields with a default value (e.g., 0)
df["power"] = df["power"].fillna(0).astype(int)  # Replace NaN with 0
df["beacons"] = df["beacons"].fillna(0).astype(int)  # Replace NaN with 0
df["channel"] = df["channel"].fillna(0).astype(int)  # Replace NaN with 0
df["iv"] = df["iv"].fillna(0).astype(int)  # Replace NaN with 0
df["idlen"] = df["idlen"].fillna(0).astype(int)  # Replace NaN with 0

# Import data into Django model
for _, row in df.iterrows():
    WifiScan.objects.create(
        bssid=row["bssid"],
        first=row["first"],
        last=row["last"],
        channel=row["channel"],
        speed=row["speed"],
        privacy=row["privacy"],
        cipher=row["cipher"],
        auth=row["auth"],
        power=row["power"],
        beacons=row["beacons"],
        iv=row["iv"],
        ip=row["ip"],
        idlen=row["idlen"],
        essid=row["essid"],
        key=row["key"]
    )

print("WiFi scan data imported successfully!")
