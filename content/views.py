from django.shortcuts import render
from .models import Project

# Create your views here.
def projects_list(request):
    projects = Project.objects.all()
    return render(request, 'content/projects_list.html', {"projects": projects})

#Create, Edit, Delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id

