"""Posts models."""

# Django
from django.db import models
#from django.contrib.auth.models import User
from users.models import Profile
class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/photos')
    caption = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username"""
        return "{} by @{}".format(self.name,self.caption, self.profile.user.username)


