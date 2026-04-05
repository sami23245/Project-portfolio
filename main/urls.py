from django.urls import path
from main import views

urlpatterns = [
    path('base',views.home, name='base'),#for base.html and tseting purpose
    path('',views.home_view, name='home'),
    path('journey/',views.journey_view, name='journey'),
    path('contact/',views.contact_view, name='contact'),
]