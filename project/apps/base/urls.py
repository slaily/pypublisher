from django.urls import path

from project.apps.base import views


urlpatterns = [
    path('', views.IndexView.as_view())
]
