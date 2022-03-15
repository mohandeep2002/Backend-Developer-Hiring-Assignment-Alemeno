from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Kid
from .forms import ImageForm, KidsForm


# Create your views here.
def home(request):
    all_kids = Kid.objects.all()

    return render(request, "index.html", {'data': all_kids})


def add_kids(request):
    # return HttpResponse('add kids page')
    if request.method == 'POST':
        form = KidsForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "Add_kids.html", {'msg': 'Response Saved'})
    else:
        form = KidsForm
        return render(request, "Add_Kids.html", {'form': form})


def add_images(request):
    # return HttpResponse('add images page')
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print(form.errors)
            return render(request, "Add_Images.html", {"msg": 'Response Saved'})
        else:
            print(form.errors)
            return HttpResponse("ELSEIF")
    else:
        form = ImageForm
        return render(request, "Add_Images.html", {"form": form})
