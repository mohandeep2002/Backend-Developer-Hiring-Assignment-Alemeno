from urllib import response
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


def add_kids(request):
    #return HttpResponse('add kids page')
    return render(request, "Add_Kids.html")

def add_images(request):
    #return HttpResponse('add images page')
    return render(request, "Add_Images.html")