from django.shortcuts import render


# Create your views here.

def home(request):#for testing and view base.html
    return render(request, 'base.html')


def home_view(request):
    return render(request, 'assets/home.html')




def journey_view(request):
    return render(request, 'assets/journey.html')


def contact_view(request):
    return render(request, 'assets/Contact.html')



