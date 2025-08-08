from django.shortcuts import render
from django.http import HttpResponse
#cretae your view here
def index(request):
    return HttpResponse("index.html")

