
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    photo = models.ImageField( upload_to='users/pictures', blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=250, blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username"""
        return self.user.username
