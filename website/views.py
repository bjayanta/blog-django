from gc import get_objects
from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Post

# Create your views here.
class Details(View):
    meta = {
        "title": "Details",
    }

    def get(self, request, slug):
        self.meta["post"] = get_object_or_404(Post, slug = slug)
        return render(request, 'website/details.html', self.meta)