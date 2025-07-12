'''Django has by default methods for creating form which is creating Form name and then in Meta class we
have all the fields as in our model class. We can also add some extra fields in our form class which are not'''

from django.forms import ModelForm
from .models import Room,Message
from django.contrib.auth.models import User  # authorized django admin user like vaibhavishah04, janhavi
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']   # This is to exclude the host and participants in the html form view


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

# we don't need to register the form in admin.py becuase it is not a model form and we are not using it in admin.py

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    
