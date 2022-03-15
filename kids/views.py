from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Kid
from .forms import ImageForm


# Create your views here.
def home(request):
    all_kids = Kid.objects.all()

    return render(request, "index.html", {'data': all_kids})


def add_kids(request):
    # return HttpResponse('add kids page')
    return render(request, "Add_Kids.html")


def add_images(request):
    # return HttpResponse('add images page')
    form = ImageForm()
    return render(request, "Add_Images.html",{'form':form})
