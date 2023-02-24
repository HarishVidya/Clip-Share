from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    clip_link = models.CharField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    def total_likes(self):
        return self.likes.count()

    def save(self):
        self.clip_link = self.clip_link[33:]
        return super().save()


# class Comment(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

#     def __str__(self):
#         return str(self.author) + ' comment ' + str(self.content)

#     @property
#     def children(self):
#         return Comment.objects.filter(parent=self).reverse()

#     @property
#     def is_parent(self):
#         if self.parent is None:
#             return True

    

    