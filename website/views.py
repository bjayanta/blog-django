from django.db.models import Q
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from .models import Post, Category
from .forms import CommentForm

# Create your views here.
class Details(View):
    meta = {
        "title": "Details",
    }

    def get(self, request, category_slug, slug):
        self.meta["post"] = get_object_or_404(Post, slug = slug, status = Post.ACTIVE)
        self.meta["form"] = CommentForm()

        return render(request, 'website/details.html', self.meta)

    def post(self, request, category_slug, slug):
        self.meta["post"] = get_object_or_404(Post, slug = slug, status = Post.ACTIVE)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.meta["post"]
            comment.save()

            return redirect('website.details', category_slug = category_slug, slug = slug)
        else:
            self.meta["form"] = CommentForm()

        return render(request, 'website/details.html', self.meta)

class CategoryView(View):
    meta = {
        "title": "Category"
    }

    def get(self, request, slug):
        self.meta["category"] = get_object_or_404(Category, slug = slug)
        self.meta["posts"] = self.meta["category"].posts.filter(status = Post.ACTIVE)
        
        return render(request, 'website/category.html', self.meta)

class SearchView(View):
    meta = {
        "title": "Search"
    }

    def get(self, request):
        query = request.GET.get('query', '')

        self.meta['query'] = query
        self.meta['posts'] = Post.objects.filter(status = Post.ACTIVE).filter(Q(title__icontains = query) | Q(content__icontains = query))

        return render(request, 'website/search.html', self.meta)