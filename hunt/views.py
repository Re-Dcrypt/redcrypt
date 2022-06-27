from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return redirect('home')
    return render(request, 'base.html')


def home(request):
    return render(request, 'base.html')
