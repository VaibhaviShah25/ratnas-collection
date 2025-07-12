from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import WifiScan, Location
from .forms import WifiForm, LocationForm
from django.db.models import Q
# Create your views here.

def display(request):
    return render(request,"gps/home.html")


def gps_html_page(request):
    return render(request, 'gps/gps_html.html')

def gps_record_page(request):
    return render(request, 'gps/recorder.html')


def gps_camera(request):
    return render(request, 'gps/camera.html')

# views.py
def addLocation(request):
    if request.method == 'POST':
        Location.objects.create(
            location_name=request.POST.get('location_name'),
            latitude=request.POST.get('latitude'),
            longitude=request.POST.get('longitude'),
            photo=request.FILES.get('photo'),
            audio=request.FILES.get('audio')
        )
        return redirect('gps_html')  # or wherever
    return render(request, 'gps/gps_html.html')


def showData(request):
    wifi_scans  = WifiScan.objects.all()
    context = {"wifi_scans":wifi_scans} 
    return render(request,'gps/gps_html.html',context)

def allData(request,essid = None):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    
    wifi_scans = WifiScan.objects.filter(essid__icontains=q)
    selected_data = None
    selected_data = WifiScan.objects.filter(essid=essid) if essid else None
    print("No essid provided")

    return render(request, 'gps/all_data.html', {
        'wifi_scans': wifi_scans,
        'selected_data': selected_data,
    })   # we are passing the essid data as well as full data so that we can see both together

def displayFullData(request,pk):
    wifi_scan  = WifiScan.objects.filter(essid = pk)   # This is used for multiple rows 
    print(wifi_scan)
    context = {"wifi_scan":wifi_scan} 
    return render(request,'gps/full_data.html',context)

def camera_stream(request):
    return render(request, 'gps/camera_stream.html')

def console(request):
    return render(request, 'gps/console.html')



def space(request):
    return render(request, 'gps/space.html')

def index(request):
    return render(request, 'gps/index_gps.html')

def error(request):
    return render(request,'gps/error_gps.html')

def intro(request):
    return render(request,'gps/intro.html')