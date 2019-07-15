from unittest import TestCase
from unittest.mock import patch, Mock

from project.apps.blog.models import Article

from project.apps.blog.views import ArticleListView


class ArticleListViewTest(TestCase):
    @patch(
        'django.views.generic.list.MultipleObjectMixin.paginate_queryset',
        return_value=(
            0,
            1,
            0,
            0
        )
    )
    @patch(
        'django.views.generic.list.MultipleObjectMixin.get_context_data',
        return_value={}
    )
    def test_get_context_data(
        self,
        mock_paginate_queryset,
        mock_get_context_data,
    ):
        article_list_view = ArticleListView()
        context = article_list_view.get_context_data()

        self.assertIn('page', context)
