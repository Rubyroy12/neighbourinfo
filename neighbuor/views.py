from django.shortcuts import render,redirect
from .forms import BusinessForm,PostForm,UpdateUserProfileForm,UpdateUserForm,NeighbourhoodForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Profile,Post,Neighbourhood
# Create your views here.
def index(request):
    neighbour=Neighbourhood.objects.all()
    posts = Post.objects.all()

    params = {
        'posts': posts,
        'neighbour':neighbour,
        
    }

    return render(request,'index.html',params )

@login_required(login_url='/accounts/login/')
def profile(request, username):
    Profile.objects.get_or_create(user=request.user)
    neighbour=Neighbourhood.objects.all()
    
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
        'neighbour': neighbour,
        
    }
    return render(request, 'profile.html', params)

def update_neighbourhood(request):
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user.profile
            update.save()
            return redirect('/',)
    else:
        form= NeighbourhoodForm()
    return render(request, 'neighbourinfo.html', {'form': form})

def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return redirect('/',)
    else:
        form= PostForm()
   
    return render(request, 'newpost.html', {'form': form})
        