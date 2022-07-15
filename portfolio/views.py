from django import views
from django.shortcuts import render
from .models import Project

# Create your views here.
def homepage(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/homepage.html', {'projects':projects})

def all_blogs(request):
    return render(request, views.all_blogs, 'blog/all_blogs.html')