from django.urls import path

from .views import ArticleDetailView, ArticleListCreateView

urlpatterns = [
    path("articles/", ArticleListCreateView.as_view(), name="article-list-create"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
]
