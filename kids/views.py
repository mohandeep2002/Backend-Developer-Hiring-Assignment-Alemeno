from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Kid
from .forms import ImageForm, KidsForm
from django.core.mail import send_mail
from django.conf import settings


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
            f = form.save()
            print(form.errors)
            if f.food_group == "Unknown":
                print("yes", f.image_id.parents_email_id)
                destination = str(f.image_id.parents_email_id)
                subject = "Unknown Category in Food Group"
                message = "Unknown Category in Food Group\nName:" + str(f.image_id.kid_name) + "\nParents Ph no:" + str(f.image_id.phone_number) + "\nKids' Age" + str(f.image_id.kid_age)
                source = settings.EMAIL_HOST_USER
                send_mail(subject, message, source, [destination,])
                print("mail sent")
            return render(request, "Add_Images.html", {"msg": 'Response Saved'})
        else:
            print(form.errors)
            return HttpResponse("ELSEIF")
    else:
        form = ImageForm
        return render(request, "Add_Images.html", {"form": form})
