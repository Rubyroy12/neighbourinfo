from django import forms
from django.db.migrations.operations import fields
from .models import Profile,Business,Post,Location,Neighbourhood
from django.contrib.auth.models import User

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ()

class NeighbourhoodForm(forms.ModelForm):
    class Meta: 
        model= Neighbourhood
        fields = ('name','name','locations','occupants')

class Business(forms.ModelForm):
    class Meta: 
        model=Business
        fields = ('name','email')
class Post(forms.ModelForm):
    class Meta: 
        model=Post
        fields = ('title','post')