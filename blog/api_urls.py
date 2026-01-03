from . import views
from django.urls import path

urlpatterns = [
    path('api/posts/',views.posts_api,name = 'api_posts'),
    path('/api/posts/<int:post_id>/',views.post_detail_api,name = 'api_post_detail'),
    path('api/post/create',views.post_detail,name= 'api_posts'),
]