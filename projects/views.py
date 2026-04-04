from django.shortcuts import render
from .models import Project

def project_list(request):
    # Fetch all projects from the database
    all_projects = Project.objects.all().order_by('-created_at')

    # Pass them to the template
    return render(request, 'assets/projects.html', {'projects': all_projects})