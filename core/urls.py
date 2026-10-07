from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("a-propos/", views.about, name="about"),
    path("racing/", views.racingpage, name="racing"),
    path("racing/<int:race_id>/", views.race_detail, name="race_detail"),
]
