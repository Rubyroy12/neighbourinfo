from django import forms
from django.db.migrations.operations import fields
from .models import Profile,Business,Post,Location,Neighbourhood
from django.contrib.auth.models import User

from neighbuor import models

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ()

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