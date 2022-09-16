from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):
    meta = {
        "title": "Index"
    }

    def get(self, request):
        return render(request, 'core/index.html', self.meta)

class AboutView(View):
    meta = {
        "title": "About"
    }

    def get(self, request):
        return render(request, 'core/about.html', self.meta)