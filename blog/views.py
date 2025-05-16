from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import permissions, viewsets

from .forms import ArticleForm, SignUpForm
from .models import Article
from .permissions import IsAuthorOrAdmin
from .serializers import ArticleSerializer


# Frontend views
def article_index(request):
    articles = Article.objects.filter(published=True)
    return render(request, "blog/index.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/detail.html", {"article": article})


@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("article-view", pk=article.pk)
    else:
        form = ArticleForm()
    return render(request, "blog/create.html", {"form": form})


@login_required
def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if not (request.user.is_staff or article.author == request.user):
        raise PermissionDenied

    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article-view", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog/edit.html", {"form": form, "article": article})


@login_required
def article_delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if not (request.user.is_staff or article.author == request.user):
        raise PermissionDenied

    if request.method == "POST":
        article.delete()
        messages.success(request, "Article deleted successfully.")
        return redirect("article-index")

    return render(request, "blog/delete.html", {"article": article})


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("article-index")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})


# API ViewSet
class ArticleViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, and destroy actions for Article.
    """

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrAdmin]

    def get_queryset(self):
        qs = super().get_queryset()
        published = self.request.query_params.get("published")
        tag = self.request.query_params.get("tag")
        date = self.request.query_params.get("date")

        if published is not None:
            qs = qs.filter(published=published.lower() == "true")
        if tag:
            qs = qs.filter(tags__icontains=tag)
        if date:
            qs = qs.filter(published_date__date=date)

        return qs

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
