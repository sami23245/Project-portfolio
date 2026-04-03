from django.urls import path
from main import views

urlpatterns = [
    path('base',views.home, name='home'),#for base.html and tseting purpose
    path('',views.home_view, name='home'),
    path('projects/',views.projects_view, name='projects'),
    path('journey/',views.journey_view, name='journey'),
    path('contact/',views.contact_view, name='contact'),
]