from django.urls import path

from .views import (
    ArticleDetailView,
    ArticleListCreateView,
    article_detail,
    article_index,
)

urlpatterns = [
    # API
    path("articles/", ArticleListCreateView.as_view(), name="article-list-create"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    # Frontend
    path("", article_index, name="article-index"),
    path("article/<int:pk>/", article_detail, name="article-view"),
]
