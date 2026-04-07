from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ReviewForm

def project_list(request):
    data_from_db = Project.objects.all()
    return render(request, 'assets/projects.html', {'projects': data_from_db})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project
            review.save()
            return redirect('project_detail', pk=pk)  # Reload same page

    reviews = project.reviews.all().order_by('-created_at')

    return render(request, 'assets/projects_details.html', {
        'project': project,
        'form': form,
        'reviews': reviews,
    })