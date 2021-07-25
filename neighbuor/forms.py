from django import forms
from django.db.migrations.operations import fields
from .models import Profile,Business,Post,Location,Neighbourhood
from django.contrib.auth.models import User

from neighbuor import models

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')
class NeighbourhoodForm(forms.ModelForm):
    class Meta: 
        model= Neighbourhood
        fields = ('name','occupants')

class BusinessForm(forms.ModelForm):
    class Meta: 
        model=Business
        fields = ('name','email')
class PostForm(forms.ModelForm):
    class Meta: 
        model=Post
        fields = ('title','post')
class LocationForm(forms.ModelForm):
    class Meta: 
        model=Location
        fields = ('name',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('name',)

class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', ]
