"""Posts Admins"""
from django.contrib import admin
from posts.models import Post
from users.models import Profile

admin.site.register(Post)
