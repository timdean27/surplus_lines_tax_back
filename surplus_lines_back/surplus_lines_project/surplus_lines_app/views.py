# views.py
from django.shortcuts import render

def hello_world(request):
    message = "Hello, World!"
    return render(request, 'main.html', {'message': message})
