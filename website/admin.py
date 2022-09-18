from django.contrib import admin
from .models import Category, Post, Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content']
    list_display = ['title', 'slug', 'category', 'created_at', 'status']
    list_filter = ['category', 'created_at', 'status']
    inlines = [CommentItemInline]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'post', 'created_at']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)