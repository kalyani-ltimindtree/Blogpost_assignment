from django.contrib import admin
from .models import CustomUser, Post, Comment


admin.site.register(Post)
admin.site.register(Comment)
