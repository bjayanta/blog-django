from django.urls import path
from .views import Details, CategoryView

urlpatterns = [
    path('<slug:category_slug>/<slug:slug>', Details.as_view(), name='website.details'),
    path('<slug:slug>/', CategoryView.as_view(), name='website.category'),
]
