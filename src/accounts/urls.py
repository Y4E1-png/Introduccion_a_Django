from django.urls import path
from accounts import views

urlpatterns = [
  path("", views.registro, name="register_form")
]