from django.urls import path
from . import views

urlpatterns = [
    path('gps/',views.display, name = "gps"),   # This is the url for myfunctionCall
                                                    # '' means default url that is GPS/
    path('gps_html/', views.gps_html_page, name='gps_html'),# for gps_html.html
    path('gps_record/', views.gps_record_page, name='gps_record'),# for recorder.html
    path('gps_camera/', views.gps_camera, name='gps_camera'),# for camera.html
    path('add-location/', views.addLocation, name='add-location'),# for adding location
    path('show-data/', views.showData, name='show-data'),# for showing data
    path('full-data/<str:pk>/', views.displayFullData, name='full-data'),
    path('all-data/', views.allData, name='all-data'),# for showing all data
    # urls.py
    path('all-data/<str:essid>/', views.allData, name='all-data-detail'),
    path('camera-stream/', views.camera_stream, name='camera-stream'),# for camera stream
    path('console/', views.console, name='console'),# for console.html
    path('index/',views.index, name='index'),
    path('space/',views.space, name='space'),# for space.html
    path('error/',views.error, name='error'),
    path('intro/',views.intro, name='intro'),# for intro.html
    

]