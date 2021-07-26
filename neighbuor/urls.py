
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/profile/<str:username>/',views.profile, name = 'profile'),
    path('neighbuor/',views.update_neighbourhood, name='neighbor'),
    path('newpost/', views.newpost, name = 'newpost'),
    path('search/$', views.search_results, name='search_results'),
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)