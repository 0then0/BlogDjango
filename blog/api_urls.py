from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet

router = DefaultRouter()
router.register(r"articles", ArticleViewSet, basename="article")

urlpatterns = [
    # This will generate:
    # GET     /api/articles/        → list
    # POST    /api/articles/        → create
    # GET     /api/articles/{pk}/   → retrieve
    # PUT     /api/articles/{pk}/   → update
    # PATCH   /api/articles/{pk}/   → partial_update
    # DELETE  /api/articles/{pk}/   → destroy
    path("", include(router.urls)),
]
