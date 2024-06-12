
from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest

def index(request: WSGIRequest):
    
    return render(request=request, template_name="index.html")
