from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest



def index(request):
    return render(request=request, template_name="student/index.html")

