from django.contrib import admin
from .models import Author, BlogPost, Comment


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "body", "created_at")
    list_filter = ("author",)
    search_fields = ("title",)
    date_hierarchy = "created_at"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("commenter_name", "post", "created_at")
    search_fields = ("commenter_name", "content")
