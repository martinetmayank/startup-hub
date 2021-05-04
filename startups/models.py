from django.contrib.auth.models import User
from django.db import models


class StartupModel(models.Model):
    startup_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    email = models.EmailField(max_length=64)
    awards = models.TextField(max_length=128, blank=True)
    youtube = models.URLField(blank=True)
    location = models.CharField(max_length=128)
