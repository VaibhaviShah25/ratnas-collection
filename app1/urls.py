from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home, name = "home"),   # This is the url for myfunctionCall
                                                 # '' means default url that is app1/
    path('login/',views.loginPage, name = "login"),  # This is the url for loginPage function
    path('logout/',views.logoutUser, name = "logout"),  # This is the url for logoutUser function
    path('register/',views.registerPage, name = "register"),  # This is the url for registerPage function
    path('profile/<str:pk>/',views.userProfile, name = "user-profile"),  # This is the url for userProfile function
    path('message/',views.createMessage, name = "create-message"),  # This is the url for createMessage function
    path('topic/',views.topicsPage, name = "topic"),  # This is the url for topicPage function
    path('activity/',views.activityPage, name = "activity"),  # This is the url for activityPage function
    path('delete-message/<str:pk>/', views.deleteMessage, name = "delete-message"),
    path('',views.display, name = "display"),  # This is the url for display function
    path('room/<str:pk>/',views.room, name = "room"),  # This is the url for room function
    path('create-room/',views.createRoom, name = "create-room"),  # This is the url for createRoom function
    path('update-room/<str:pk>', views.updateRoom, name = "update-room"),
    path('delete-room/<str:pk>', views.deleteRoom, name = "delete-room"), 
    path('user-update/', views.updateUser, name = "user-update"),
]   