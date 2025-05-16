from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True, blank=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title
