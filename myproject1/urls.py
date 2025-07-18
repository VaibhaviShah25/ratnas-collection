"""
URL configuration for myproject1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
#from debug_toolbar.conf import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1',include('app1.urls')),
    path('myfirstapp/',include('myfirstapp.urls')),   # to include all urls from myfirstapp
    path('',include('gps.urls')),                 # to include all urls from gps
    path('api/',include('myfirstapp.api.urls')),                 # to include all urls from api
    path('clotheweb/',include('clotheweb.urls')),                 # to include all urls from clotheweb
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)