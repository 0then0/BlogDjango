from rest_framework import generics

from .models import Article
from .serializers import ArticleSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        published = self.request.query_params.get("published")
        tag = self.request.query_params.get("tag")
        date = self.request.query_params.get("date")

        if published is not None:
            queryset = queryset.filter(published=published.lower() == "true")
        if tag:
            queryset = queryset.filter(tags__icontains=tag)
        if date:
            queryset = queryset.filter(published_date__date=date)

        return queryset


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
