import builtins
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
from cloudinary.models import CloudinaryField 
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    name = models.CharField(blank=True, max_length=120)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    @classmethod
    def profile(cls):
        profiles = cls.objects.all()
        return profiles

    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def save_profile(self):
        self.user

    def __str__(self):
        return self.name

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()
   
  
class Location(models.Model):
    user = models.ForeignKey(Profile,on_delete = models.CASCADE,related_name='location',null = True)
    name = models.CharField(max_length = 50)

class Neighbourhood(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'neighbour')
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    occupants = models.IntegerField(null=True)

    
   
    # def create_neighbourhood(self):
    #     pass
    
    def delete_neighbourhood(self):
        self.delete()

    # @classmethod
    # def find_neighbourhood(neighbourhod_id):
    #     neighbour= Neighbourhood.objects.filter(title__icontains=)
    #     return neighbour
    # @classmethod
    # def update_neighbourhood(self):
    #     pass



class Business(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    neighbourhood= models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email= models.EmailField(max_length=50)

    def delete_business(self):
        self.delete()

    def find_business(business_id,self):
        business = Business.objects.get(id=business_id)
        return business


    @classmethod
    def update_business():
        pass
        

    @classmethod
    def search_business(cls, search_term):
        business= cls.objects.filter(title__icontains=search_term)
        return business
    
    def __str__(self):
        return self.name


class Post(models.Model):
    title=models.CharField(max_length= 100)
    post= models.TextField(max_length=300)
    image = CloudinaryField('image')
    posted= models.DateField(auto_now_add=True)

  
    def save_post(self):
        self.save()
  
    def delete_post(self):
        self.delete()






