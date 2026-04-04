from django.shortcuts import render

# Create your views here.

def home(request):#for testing and view base.html
    return render(request, 'base.html')


def home_view(request):
    return render(request, 'mainhome.html')


def projects_view(request):
    return render(request, 'main/projects.html')


def journey_view(request):
    return render(request, 'main/journey.html')


def contact_view(request):
    return render(request, 'main/Contact.html')