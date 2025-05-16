from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from rest_framework import generics, viewsets

from .forms import ArticleForm
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


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

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


def article_index(request):
    articles = Article.objects.filter(published=True)
    return render(request, "blog/index.html", {"articles": articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "blog/detail.html", {"article": article})


def article_create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("article-index"))
    else:
        form = ArticleForm()
    return render(request, "blog/create.html", {"form": form})


def article_edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("article-view", pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    return render(request, "blog/edit.html", {"form": form, "article": article})
