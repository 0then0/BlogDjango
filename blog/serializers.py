from rest_framework import serializers

from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = [
            "id",
            "author",
            "title",
            "content",
            "published",
            "published_date",
            "tags",
        ]
