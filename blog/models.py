from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.published and self.published_date is None:
            self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
