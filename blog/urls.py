from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_posts,name = 'list_posts'),
    path('posts/create/',views.create_posts,name = 'create_posts'),
    path('posts/<int:post_id>/',views.post_detail,name = 'post_detail'),
    path('posts/<int:post_id>/comments/',views.add_comments,name = 'add_comment'),
    path('author/<int:author_id>/posts/',views.author_post,name = 'author_post'),
    path('api/posts/',views.posts_api,name = 'api_posts'),
    path('api/posts/<int:post_id>/',views.post_detail_api,name = 'api_post_detail'),
    path('api/post/create',views.posts_api,name= 'api_posts'),
]