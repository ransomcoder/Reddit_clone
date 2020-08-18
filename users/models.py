from django.db import models
from django.contrib.auth.models import AbstractUser
from community.models import Community


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    karma = models.IntegerField(default=1)
    communities = models.ManyToManyField(Community, blank=True)

    def __str__(self):
        return f'u/{self.username}'
