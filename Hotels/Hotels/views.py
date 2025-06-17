from django.shortcuts import HttpResponse,render
from django.http import request 

def Home(request):
    return render(request,"Home.html")


def index(request):
    return render(request,"index.html")