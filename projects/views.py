from django.shortcuts import render, redirect,get_object_or_404
from .models import Project
from .forms import ReviewForm

def project_list(request):
    # Fetch all records from your MySQL 'Project' table
    data_from_db = Project.objects.all() 
    
    # Send the data to the template. 
    # 'projects' is the label the HTML will use to find 'data_from_db'
    return render(request, 'assets/projects.html', {'projects': data_from_db} )

def project_review(request, pk):
    # Fetch the specific project by primary key (id)
    project = Project.objects.get(pk=pk)

    # If the form is submitted

    # forms = ReviewForm(request.POST)
    if request.method == 'POST':
        if forms.is_valid():
            review = forms.save(commit=False)
            review.project = project
            review.save()
            return redirect('project_list')  # Redirect to the project list after submitting the review
    else:
        forms = ReviewForm()

    # Pass it to the template
    return render(request, 'assets/projects_details.html', 
                {'project': project, 
                'form': forms})