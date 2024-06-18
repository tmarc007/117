from django.urls import path
from . import views 

urlpatterns = [
    path("", views.projects_list, name="projects_list"),
]

#Create, Edit, Delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id