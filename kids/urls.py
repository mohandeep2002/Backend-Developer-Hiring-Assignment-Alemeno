from django.urls import path
from .views import home, add_kids, add_images
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name="home"),
    path('add_kids/', add_kids, name="add_kids"),
    path('add_images/', add_images, name="add_images")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
