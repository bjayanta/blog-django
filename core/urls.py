from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import *

urlpatterns = [
    path('about/', AboutView.as_view(), name='website.about'),
    path('', include('website.urls')),
    path('', IndexView.as_view(), name='website.index'),
]
