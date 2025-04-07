from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.http import Http404
# Create your views here.
pjcs = [
    {
        'id': 1,
        'title': 'My personal portfolio',
        'description': 'this is a desc 1, for the first project'
    },
    {
        'id': 2,
        'title': 'sklepy web site',
        'description': 'this is a desc 2, another project'
    },
    {
        'id': 3,
        'title': 'sklepy web site',
        'description': 'this is a desc 2, another project'
    },
    {
        'id': 4,
        'title': 'sklepy web site',
        'description': 'this is a desc 2, another project'
    },
    {
        'id': 5,
        'title': 'sklepy web site',
        'description': 'this is a desc 2, another project'
    },
    {
        'id': 6,
        'title': 'sklepy web site',
        'description': 'this is a desc 2, another project'
    },
]

# Create your views here.
def projects(response):
    return render(response, 'projects/projects.html', {'projects': pjcs})

def project(request, id):
    p = {}
    valid = False
    for project in pjcs:
        if project['id'] == id:
            p = project
            valid = True
            break

    if valid:
        return render(request, 'projects/project.html', {'project': p})
    else:
        raise  Http404()
    

def default(request, id):
    url = reverse('project', args=[id])
    return HttpResponseRedirect(url)