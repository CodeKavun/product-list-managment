from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello(request):
    return HttpResponse("Hello everyone!")

def about(request):
    return render(request, 'about_project.html')

def about_core(request):
    return render(request, 'core/about_core.html')
