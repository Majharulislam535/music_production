from django.shortcuts import render,redirect
from .import forms
from .models import Album_models
# Create your views here.


def album(request):
    if request.method=='POST':
       form = forms.Album(request.POST)
       if form.is_valid():
         form.save()
         return redirect('home')
    else:
        form = forms.Album()
    return render(request,'album.html',{'form':form})

def edit_album(request,id):
    album = Album_models.objects.get(pk=id)

    form = forms.Album(instance=album)
    if request.method=='POST':
       form = forms.Album(request.POST,instance=album)
       if form.is_valid():
         form.save()
         return redirect('home')
     
    return render(request,'album.html',{'form':form})