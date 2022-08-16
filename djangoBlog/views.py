from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    # return HttpResponse('hello world, its first jango project')
    return render(request , "about.html")


def Home(request):
    # return HttpResponse('hello world, its first jango project')
    return render(request , 'Home.html')
