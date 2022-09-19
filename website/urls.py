from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import Details, CategoryView, SearchView

urlpatterns = [
    path('search/', SearchView.as_view(), name='website.search'),
    path('<slug:category_slug>/<slug:slug>', Details.as_view(), name='website.details'),
    path('<slug:slug>/', CategoryView.as_view(), name='website.category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
