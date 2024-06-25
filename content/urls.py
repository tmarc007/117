from django.urls import path
from . import views 

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.projects_list, name="projects_list"),

    path("new/", views.project_new, name="project_new"),
]



urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

#Create, Edit, Delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id