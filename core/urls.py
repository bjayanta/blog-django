from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='website.index'),
    path('about/', AboutView.as_view(), name='website.about'),
]
