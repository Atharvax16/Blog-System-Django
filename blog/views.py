from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from .models import Author,Comment,BlogPost
from .forms import BlogPostForm,CommentForm
from django.http import JsonResponse
import json

def list_posts(request):
    posts = BlogPost.objects.select_related('author').order_by('-created_at')
    return render(request,'list_posts.html',{'posts':posts})

def create_posts(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('list_posts')
    else:
        form = BlogPostForm()
    return render(request,'post_form.html',{'form':form})
        
def post_detail(request,post_id):
    post = get_object_or_404(BlogPost.objects.select_related('author'),id = post_id)
    comments = post.comments.all()
    return render(request,'post_detail.html',{'post':post,"comments":comments})

def add_comments(request,post_id):
    post = get_object_or_404(BlogPost,id = post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail',post_id = post.id)
        
    else:
        form = CommentForm()
    return render(request,'comment_form.html',{'post':post,'form':form})
        

def author_post():
    return HttpResponse()



def posts_api(request):
    if request.method == 'GET':
        posts = BlogPost.objects.select_related('author').order_by('-created_at')
        data = [
            {
                'id' : p.id,
                'title' : p.title,
                'body' : p.body,
                'author':{
                    'id' : p.author_id,
                    'name' : p.author.name,
                },
                'created_at':p.created_at.isoformat(),
            }
            for p in posts
        ]
        return JsonResponse(data,safe = False,status = 200)
    elif request.method == 'POST':
        try:
            payload = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error':'Invalid JSON'},status = 400)
        
        title = payload.get('title')
        author_id = payload.get('author_id')
        body = payload.get('body','')

        if not title or not author_id:
            return JsonResponse({'error':'Missing required fields:title,author_id'},
                                status = 400)
        
        author = get_object_or_404(Author,id = author_id)
        post = BlogPost.objects.create(title = title,body = body,author = author)

        data = {
            "id":post.id,
            "title":post.title,
            "body":post.body,
            "author":{
                'id': post.author_id,'name':post.author.name
            },
            'created_at':post.create_at.isoformat(),
        }
        return JsonResponse(data,status = 201)
    return JsonResponse({'error':"Method not allowed"},status = 405)

def post_detail_api(request,post_id):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    post = get_object_or_404(
        BlogPost.objects.select_related("author"),
        id=post_id
    )

    data = {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "author": {
            "id": post.author_id,
            "name": post.author.name,
        },
        "created_at": post.created_at.isoformat(),
    }

    return JsonResponse(data, status=200)