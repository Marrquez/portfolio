from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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
    colors = ['red', 'blue', 'pink']
    context = {'name': name, 'colors': colors}
    return render(request, 'test.html', context)