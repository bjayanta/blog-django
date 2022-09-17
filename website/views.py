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
        self.meta["post"] = get_object_or_404(Post, slug = slug)
        self.meta["form"] = CommentForm()

        return render(request, 'website/details.html', self.meta)

    def post(self, request, category_slug, slug):
        self.meta["post"] = get_object_or_404(Post, slug = slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.meta["post"]
            comment.save()

            return redirect('website.details', slug = slug)
        else:
            self.meta["form"] = CommentForm()

        return render(request, 'website/details.html', self.meta)

class CategoryView(View):
    meta = {
        "title": "Category"
    }

    def get(self, request, slug):
        self.meta["category"] = get_object_or_404(Category, slug = slug)
        return render(request, 'website/category.html', self.meta)