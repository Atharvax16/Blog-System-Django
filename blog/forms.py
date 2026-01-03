# we use forms for handling validation,security and html generation so i dont manually trust request.post

from django import forms
from .models import BlogPost,Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title','body','author']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['commenter_name','content']