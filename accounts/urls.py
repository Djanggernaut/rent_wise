from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register-user/", views.register_user, name="register_user"),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
