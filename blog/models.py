from django.db import models



#  AUTHOR ---> BLOGPOSTS ---> COMMMENTS   

class Author(models.Model):
    name = models.TextField()
    email = models.EmailField()
    bio = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Author,on_delete = models.CASCADE)
    body = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    commenter_name = models.TextField()
    post = models.ForeignKey(BlogPost,on_delete = models.CASCADE,related_name =  'comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Comment by {self.commenter_name} on  {self.post_id}"

