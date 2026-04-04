from django.contrib import admin

# Register your models here.


from django.contrib import admin
from .models import Project, Review

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'average_rating')
    search_fields = ('title', 'tech_stack')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'project', 'rating', 'created_at')
    list_filter = ('rating', 'project')