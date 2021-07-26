from django.contrib import admin
from .models import Business,Neighbourhood,Policeinfo,Healthinfo
# Register your models here.
admin.site.register(Business)
admin.site.register(Neighbourhood)
admin.site.register(Healthinfo)
admin.site.register(Policeinfo)
