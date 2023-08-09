from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + self.content


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    comment_by = models.ManyToManyField(CustomUser)
    comment = models.CharField(max_length=300, )

    def __str__(self):
        return '%s - %s' % (self.post, self.comment)
