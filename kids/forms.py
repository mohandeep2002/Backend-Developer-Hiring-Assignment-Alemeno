from django.forms import fields
from .models import Images
from django import forms
class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        #fields = "__all__"
        fields = ['image_url']
