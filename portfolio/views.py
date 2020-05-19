from django.shortcuts import render
from django.http import HttpResponse
from personal_portfolio import settings
from .models import Project
# Create your views here.

def basic(request):
    print(settings.SECRET)
    return render(request,'portfolio/basic.html')

def home(request):
    projects=Project.objects.all()
    #take all the project objects and pass to html
    return render(request,'portfolio/home.html',{'projects':projects})

def projects(request):
    projects = Project.objects.all()
    return render(request,'portfolio/projects.html',{'projects':projects})