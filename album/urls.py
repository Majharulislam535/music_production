from django.urls import path,include
from .import views

urlpatterns = [
    path('add_album/',views.album,name='add_album'),
    path('edit_album/<int:id>',views.edit_album,name='edit_album'),
]