from django.db import models


class AddForm(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    email = models.EmailField(max_length=64)
    awards = models.TextField(max_length=128)
    youtube = models.URLField()
    linkedin = models.URLField()
    twitter = models.URLField()
    facebook = models.URLField()
    instagram = models.URLField()
    location = models.CharField(max_length=128)
