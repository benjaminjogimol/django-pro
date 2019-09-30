from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def indexpage(request):
    return HttpResponse("Welcome to my site")
def contactpage(request):
    return HttpResponse("contact page")
def homepage(request):
    return HttpResponse("Welcome to Home page")
def applyonline(request):
    return HttpResponse("Details will be published Soon!!!!")