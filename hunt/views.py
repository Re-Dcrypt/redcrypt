from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request, 'base.html')

def offline(request):
    return render(request, 'offline.html')