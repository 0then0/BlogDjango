from django.urls import path

from .views import (
    article_create,
    article_detail,
    article_edit,
    article_index,
)

urlpatterns = [
    path("", article_index, name="article-index"),
    path("article/<int:pk>/", article_detail, name="article-view"),
    path("create/", article_create, name="article-create"),
    path("article/<int:pk>/edit/", article_edit, name="article-edit"),
]
