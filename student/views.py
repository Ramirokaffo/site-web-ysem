from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.models import User
from course.models import Course

def index(request):
    student = User.objects.first()
    context = {
        "student": student,
        "selected_tab": "home"
        }
    
    return render(request=request, template_name="student/index.html", context=context)


def course(request):
    student = User.objects.first()
    courses = Course.objects.filter()

    context = {
        "student": student,
        "courses": courses,
        "selected_tab": "course"
        }
    return render(request=request, template_name="student/course.html", context=context)


def lecturer(request):
    student = User.objects.first()
    context = {
        "student": student,
        "selected_tab": "lecturer"
        }
    return render(request=request, template_name="student/lecturer.html", context=context)


def mark(request):
    student = User.objects.first()
    context = {
        "student": student,
        "selected_tab": "mark"
        }
    return render(request=request, template_name="student/mark.html", context=context)

def preference(request):
    student = User.objects.first()
    context = {
        "student": student,
        "selected_tab": "preference"
        }
    return render(request=request, template_name="student/preference.html", context=context)

