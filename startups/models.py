from django.contrib.auth.models import User
from django.db import models
from datetime import date


class StartupModel(models.Model):
    startup_user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=32)
    date_added = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=256)
    email = models.EmailField(max_length=64)
    image = models.ImageField(upload_to='images/')
    awards = models.TextField(max_length=128, blank=True)
    youtube = models.URLField(blank=True)
    location = models.CharField(max_length=128)
