from django.shortcuts import render,redirect
from .import forms
from .import models
# Create your views here.


def musician(request):
    if request.method=='POST':
       form = forms.Musician(request.POST)
       if form.is_valid():
         form.save()
         return redirect('home')
    else:
        form = forms.Musician()
        
    return render(request,'musician.html',{'form':form})
 

def edit_musician(request,id):
    musician = models.Musicians_Model.objects.get(pk=id)
    form = forms.Musician(instance=musician)
    if request.method=='POST':
       form = forms.Musician(request.POST,instance=musician)
       if form.is_valid():
         form.save()
         return redirect('home')
     
    return render(request,'musician.html',{'form':form})



def delete_musician(request,id):
    musician = models.Musicians_Model.objects.get(pk=id)
    musician.delete()
    return redirect('home')