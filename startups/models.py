from django.db import models
import uuid


class StartupModel(models.Model):
    # uid = models.UUIDField(primary_key=True,
    #                        editable=False,
    #                        blank=False,
    #                        default=uuid.uudi4)
    uid = models.CharField(
        max_length=100,
        default=uuid.uuid4().hex,
        primary_key=True)
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    email = models.EmailField(max_length=64)
    awards = models.TextField(max_length=128, blank=True)
    youtube = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    location = models.CharField(max_length=128)
