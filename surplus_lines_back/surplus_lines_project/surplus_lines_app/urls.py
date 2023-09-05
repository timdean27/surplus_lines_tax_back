# urls.py (inside your app directory)
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.hello_world, name='hello_world'),
]
