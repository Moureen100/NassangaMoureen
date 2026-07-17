from django.contrib import admin
from django.urls import path
from .form import InputForm
from .views import index
from .view import home_view
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
]
