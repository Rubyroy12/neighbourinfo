from django.shortcuts import render,redirect
from .forms import BusinessForm,PostForm,LocationForm,UpdateUserProfileForm,UpdateUserForm,NeighbourhoodForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.
def index(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form =LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('/')

    else:
        form = LocationForm()

    return render(request,'index.html', {'form': form})

@login_required(login_url='/accounts/login/')
def profile(request, username):
    Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,
        
    }
    return render(request, 'profile.html', params)

def update_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect('/',)
    else:
        form= NeighbourhoodForm()
    return render(request, 'neighbourinfo.html', {'form': form})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            update = form.save(commit=False)
            update.save()
            return redirect('/',)
    else:
        form= PostForm()
   
    return render(request, 'newpost.html', {'form': form})
        