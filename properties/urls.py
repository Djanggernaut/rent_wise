from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register-property", views.register_property, name="register_property"),
    path("edit-property/<int:pk>/", views.edit_property, name="edit_property"),
    path("delete-property/<int:pk>/", views.delete_property, name="delete_property"),
]
