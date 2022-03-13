from django.urls import path
from .views import home, add_kids, add_images
urlpatterns = [
    path('', home, name="home"),
    path('add_kids/', add_kids, name="add_kids"),
    path('add_images/', add_images, name="add_images")
]