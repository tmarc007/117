from django.shortcuts import render

# Create your views here.
def projects_list(request):
    return render(request, "content/projects_list.html")

#Create, Edit, Delete... Project
# localhost/content/projects
# localhost/content/new
# localhost/content/edit_id

