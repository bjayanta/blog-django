from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:slug>/', Details.as_view(), name='website.details'),
]
