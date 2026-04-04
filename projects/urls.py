from django.urls import path
from projects import views

# This variable name MUST be exactly 'urlpatterns' (plural)
urlpatterns = [
    path('projects/', views.project_list, name='project_list'),

    path('projects/<int:pk>/', views.project_review, name='project_detail'),
]