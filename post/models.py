from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from community.models import Community
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=3000)
    description = RichTextUploadingField(blank=True, null=True)
    date_time_posted = models.DateTimeField(default=timezone.now)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='post_likes')

    def __str__(self):
        return f'{self.title}'
