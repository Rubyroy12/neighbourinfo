
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name = 'index'),
    path('accounts/profile/<str:username>/',views.profile, name = 'profile'),
    path('neighbuor/',views.update_neighbourhood, name='neighbor'),
    path('newpost/', views.newpost, name = 'post'),
    path('posts/<id>',views.posts, name = 'posts')
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)