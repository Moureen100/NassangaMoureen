
from django.urls import path
from .Views import Myfirstproject

urlpatterns = [
    path('',  Myfirstproject, name='home'),
]
