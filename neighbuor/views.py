from django.shortcuts import render,redirect
from .forms import NeighbourhoodForm,BusinessForm,PostForm,LocationForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
    if request.method == 'POST':
        form =LocationForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('profile')

    else:
        form = LocationForm()

    return render(request,'index.html', {'form': form})

def profile(request):
    if request.method == 'POST':
        form =NeighbourhoodForm(request.POST)
        if form.is_valid():
            location = form.save(commit=False)
            location.save()
            return redirect('profile')

    else:
        form = NeighbourhoodForm()

    return render(request,'profile.html' , {'form': form})