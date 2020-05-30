from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homePage(request):
    # return HttpResponse('<h1>Hello Yoel Robotics</h1>')
    return render(request, 'school/home.html')

def aboutPage(request):
    return render(request, 'school/about.html')

def contactUs(request):
    return render(request, 'school/contact.html')