from django.urls import path

from project.apps.blog import views


urlpatterns = [
    path(
        'articles',
        views.ArticleListView.as_view(),
        name='blog-article-list-view'
    ),
    path(
        'articles/<slug:slug>',
        views.ArticleDetailView.as_view(),
        name='blog-article-detail-view'
    )
]
