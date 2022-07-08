from django.db import models
from django.utils import timezone
from datetime import timedelta as td
from django.conf import settings


# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    first_name = models.CharField(null=True, max_length=1)
    last_name= models.CharField(null=True, max_length=1)

    avatar = models.ImageField(null=True, default="avatar.svg")

    login_count = models.BigIntegerField(default=0)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def is_online(self) -> bool :
        too_old_time = timezone.now() - td(seconds=settings.LAST_ACTIVITY_INTERVAL_SECS)
        return False if self.last_login < too_old_time else True


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    host =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-updated', '-created']


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]

    class Meta:
        ordering = ['-updated', '-created']