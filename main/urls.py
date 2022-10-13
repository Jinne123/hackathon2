from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("location/", views.location, name="location"),
    path("route/", views.route, name="route"),
    path("progress/", views.progress, name="progress"),
]
