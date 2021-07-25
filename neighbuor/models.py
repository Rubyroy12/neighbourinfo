from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(max_length=50)
    # location = models.Point

class Neighbourhood(models.Model):
   class Neighborhood(models.Model):
    name = models.CharField(max_length = 50)
    location = models.ForeignKey('Location',on_delete = models.CASCADE,null = True)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    occupants = models.IntegerField(null=True)

    
    @classmethod
    def create_neighbourhood(cls):
        pass
    @classmethod
    def delete_neighbourhood(self):
        self.save()

    # @classmethod
    # def find_neighbourhood(neighbourhod_id):
    #     neighbour= Neighbourhood.objects.filter(title__icontains=)
    #     return neighbour
    @classmethod
    def update_neighbourhood():
        pass

class Location(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)


class BUsiness(models.Model):
    user=models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    neighbourhood= models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email= models.EmailField(max_length=50)



    @classmethod
    def create_business(self):

        pass

    @classmethod
    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(business_id):
        pass
    @classmethod
    def update_business():
        pass

    @classmethod
    def search_business(cls, search_term):
        business= cls.objects.filter(title__icontains=search_term)
        return business


 






