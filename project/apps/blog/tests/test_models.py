from django.test import SimpleTestCase

from project.apps.blog import models


class AuthorTest(SimpleTestCase):
    def test_str_dunder(self):
        author = models.Author(_id=1)
        author_dunder_str_format = '<Author: ID - {id}>'.format(id=author._id)

        self.assertMultiLineEqual(
            author.__str__(),
            author_dunder_str_format
        )


class ArticleTest(SimpleTestCase):
    def test_str_dunder(self):
        article = models.Article(_id=1)
        article_dunder_str_format = '<Article: ID - {id}>'.format(id=article._id)

        self.assertMultiLineEqual(
            article.__str__(),
            article_dunder_str_format
        )
