from django.urls import path, include
from .views import ProductApiView, TestViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("test-viewset", TestViewSet, basename="test-viewset")

urlpatterns = [
  path("", ProductApiView.as_view(), name="api_view"),
  path("", include(router.urls))
]