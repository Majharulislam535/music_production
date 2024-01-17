from django.shortcuts import render
from album.models import Album_models


def home(request):
    
    album = Album_models.objects.all()
    return render(request,'index.html',{'data':album})