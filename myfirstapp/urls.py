from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctionCall, name = "index"),   # This is the url for myfunctionCall
                                                     # '' means default url that is myfirstapp/
    path('about/',views.myfunctionAbout, name = "about"),
]