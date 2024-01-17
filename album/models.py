from django.db import models
from musicians.models import Musicians_Model
# Create your models here.

class Album_models(models.Model):
    CHOICE={
        '1':'1',
        '2':'2',
        '3':'3',
        '4':'4',
        '5':'5',
    }
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating=models.CharField(max_length=5, choices=CHOICE)
    musician = models.ForeignKey(Musicians_Model, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.album_name}'