from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.http import HttpResponse
from .models import Room, Topic, Message, CustomUserUpdateForm
from django.contrib import messages
from .forms import RoomForm, MessageForm
from django.db.models import Q

# Create your views here.
'''
rooms = [
    {"id":1,"name":"Manali","status":"Available"},
    {"id":2,"name":"Shimla","status":"Available"},
    {"id":3,"name":"Leh Ladakh","status":"Available"},
    
]'''
# "rooms" tells us that with what name -| 
# rooms dictionary will be accessible in index.html
# also this dictionary {"rooms" : rooms} can also be passed directly in return render method


def display(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) | 
        Q(descriptor__icontains=q) 
    )
    topics = Topic.objects.all()
    room_messages = Message.objects.filter(Q(room__name__contains=q))
    last_two_messages = room_messages[max(0, room_messages.count() - 2):]
    
    context = {"rooms": rooms, "topics": topics, "room_messages": room_messages, "last_two_messages": last_two_messages}                          
    return render(request, "index_old.html", context)


@login_required(login_url='login')  # This is used to check if the user is logged in or not. If the user is logged in, it will show the logout button and user perform the function like creating the room and if not, it will show the login button.
def createRoom(request):
    form = RoomForm()
    topic = Topic.objects.all()
    
    if request.method == "POST": # POST method is used to send data from client to server
        form = RoomForm(request.POST)   # This is done directly because we have created a form class in forms.py
                                        # Django form creation has in built to save the data directly in the server
        if form.is_valid():
            room = form.save(commit=False)
            room.host = request.user
            room.save()
            return redirect('display')
    context = {"form":form,"topics":topic}
    return render(request,"create_room_old.html",context)

@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)
    if request.method == "POST":                        # This is to update the data and send it to the server
        form = RoomForm(request.POST,instance = room)   # instance = room is used to have the same 
                                                        #data in the form and request.POST 
                                                       #will send the changed as well as the unchanged data to the table
        if form.is_valid():
            form.save()
            return redirect('display')
    context = {"form":form, "room" : room}
    
    return render(request,"room_form_old.html",context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id = pk)
    if request.method == "POST":
        room.delete()
        return redirect('home')
    return render(request,"delete_old.html",{"obj":room})


def loginPage(request):
    if request.method == "POST": # Checking this condition is important because by default request.method is GET which returns None value in request.POST.get('username')
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            User.objects.get(username=username)
        except:
            messages.error(request,"User does not exist")
        user = authenticate(request,username=username,password=password)   # authenticate is used to check if the user is valid or not
        if user is not None:                                                # if user is valid it returns User object else it returns None
            login(request,user)  
            return redirect('display')
        else:
            messages.error(request,"Username or Password is incorrect")
        
    context = {}
    return render(request,"login_register_old.html",{"page":"login"})  # This is used to show the login page. The page is passed in the context so that we can use it in the template to show the login form.

def logoutUser(request):
    logout(request)
    return redirect('display')  

def registerPage(request):
    form = UserCreationForm() # this is the default form provided by django for user registration
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False) # commit = False means we need to work on current user object and not save it in the database
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('display')
        else:
            messages.error(request,"An error occured during registration")
    return render(request,"login_register_old.html",{"page":"register","form":form})  # This is used to show the register page. The page is passed in the context so that we can use it in the template to show the register form.

def room(request,pk):
    room = Room.objects.get(id = pk)
    room_messages = room.message_set.all()
    if request.method == "POST":
        message = Message.objects.create(
            host = request.user,
            room = room,
            text = request.POST.get('body')
        )
        message.save()
        return redirect('room',pk=room.id)
    context = {'rooms':room,'room_messages':room_messages,'len':len(room_messages)}
    return render(request,'room_old.html',context)

def userProfile(request,pk):
    user = User.objects.get(id = pk) # This is to fetch the ID of the proper user
    context = {"user":user}
    return render(request,'profile_old.html',context)

def createMessage(request):
    context = {"form":MessageForm()}
    if request.method == "POST": # POST method is used to send data from client to server
        form = MessageForm(request.POST)   # This is done directly because we have created a form class in forms.py
                                        # Django form creation has in built to save the data directly in the server
        if form.is_valid():
            form.save()
            return redirect('display')
    return render(request,"create_message_old.html",context)

def deleteMessage(request,pk):
    room_message = Message.objects.get(id = pk)
    if request.method == "POST":
        room_message.delete()
        return redirect('display')
    return render(request,"delete_message_old.html",{"obj":room_message})

def home(request):
    return render(request,"home.html")  # This is used to check if the user is logged in or not. If the user is logged in, it will show the logout button and if not, it will show the login button.


@login_required(login_url='login')
def updateUser(request):
    if request.method == 'POST':
        form = CustomUserUpdateForm(instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk=request.user.id)
    else:
        form = CustomUserUpdateForm(instance=request.user)

    return render(request, 'user_update.html', {'form': form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request,"topics_old.html",{"topics":topics})


def activityPage(request):
    room_messages = Message.objects.all()
    context = {"room_messages":room_messages}
    return render(request,"activity_old.html",context)  