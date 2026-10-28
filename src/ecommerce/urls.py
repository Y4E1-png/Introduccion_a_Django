
from django.urls import path
from ecommerce import views
from ecommerce.views import ProtectedListView

urlpatterns = [
    path("", views.list_view, name="list"),
    path("<int:product_id>", views.detail_view, name="detail"),
    path("create", views.create_view, name="create"),
    path("<int:product_id>/edit/", views.update_view, name="update"),
    path("<int:product_id>/delete/", views.delete_view, name="delete"),
    path("my-products", ProtectedListView.as_view(), name="protected-list")
]