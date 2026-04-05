from django.urls import path
from main import views
from projects import views as project_views

urlpatterns = [
    path('base',views.home, name='home'),#for base.html and tseting purpose
    path('',views.home_view, name='home'),
    path('projects_1/',project_views.project_list, name='projects_list'),
    path('journey/',views.journey_view, name='journey'),
    path('contact/',views.contact_view, name='contact'),
]