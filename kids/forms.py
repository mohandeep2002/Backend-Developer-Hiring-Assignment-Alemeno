from django.forms import fields
from .models import Images, Kid
from django import forms


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        # fields = "__all__"
        fields = ['image_id', 'food_image', 'food_group']


class KidsForm(forms.ModelForm):
    class Meta:
        model = Kid
        fields = "__all__"
