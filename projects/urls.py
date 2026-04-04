from django.urls import path
from projects import views

# This variable name MUST be exactly 'urlpatterns' (plural)
urlpatterns = [
    path('', views.project_list, name='project_list'),
]