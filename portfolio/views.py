from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from projects.models import Project

def home(request):
    return render(request, 'index.html')

# def home(request):
#     return HttpResponse("Hola mundo")

def default(request, path):
    url = reverse('test', args=[path])
    return HttpResponseRedirect(url)

def index(request):
    url = reverse('home')
    return HttpResponseRedirect(url)

def test(request, name=''):
    ########################
    # to create/add model

    # option 1: using constructor:
    # project = Project(title="Test project", description='Test project desc', iconName='book')
    # project.save()
    
    # option 2: using object, this automatically save the object
    # project = Project.objects.create(title="Test project", description='Test project desc', iconName='book')
   
    # end createModel
    ########################

    ########################
    # to delete model

    # option 1: find the object by id and then delete it
    # project = Project.objects.get(id=9)
    # project.delete()

    # option 2: using object, this directly delete without instance of object
    # Project.objects.filter(id=10).delete()
    
    # end deleteModel
    ########################

    colors = ['red', 'blue', 'pink']
    context = {'name': name, 'colors': colors}
    return render(request, 'test.html', context)