from django.shortcuts import render
from django.views import View
from website.models import Post
from django.core.paginator import Paginator

# Create your views here.
class IndexView(View):
    meta = {
        "title": "Index",
    }

    def get(self, request):
        posts = Post.objects.filter(status = Post.ACTIVE)
        page = Paginator(posts, 10)

        self.meta['posts'] = page.get_page(request.GET.get('page'))

        return render(request, 'core/index.html', self.meta)

class AboutView(View):
    meta = {
        "title": "About"
    }

    def get(self, request):
        return render(request, 'core/about.html', self.meta)