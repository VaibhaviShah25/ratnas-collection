from django.db import models
from django import forms
from django.contrib.auth.models import User  # authorized django admin user like vaibhavishah04, janhavi

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name 
    

class Room(models.Model): 
    # Yaha host hi user hai
    name = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    descriptor = models.TextField(null=True,blank=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null = True)  
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id','-created']

    def __str__(self):
        return self.name
    
class Message(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null = True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField(null=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-id','-created']
    
    def __str__(self):
        return self.text[:]



# we don't need to register the form in admin.py becuase it is not a model form and we are not using it in admin.py
class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
    