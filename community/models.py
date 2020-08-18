from django.db import models
from django.utils import timezone
from django.conf import settings


class Community(models.Model):
    name = models.CharField(max_length=50)
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_time_created = models.DateTimeField(default=timezone.now)
    desc = models.TextField(max_length=3000)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='community_members')

    def __str__(self):
        return f'c/{self.name}'
