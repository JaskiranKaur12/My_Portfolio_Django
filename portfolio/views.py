from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
# Create your views here.

def home(request):
    projects=Project.objects.all()
    #take all the project objects and pass to html
    return render(request,'portfolio/home.html',{'projects':projects})