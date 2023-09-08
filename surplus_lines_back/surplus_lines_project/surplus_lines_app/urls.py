# surplus_lines_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_world'),  # Define the URL pattern for hello_world view
]
