from django.db import models

from project.apps.base.models import Base


class Author(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return '<Author: ID - {id}>'.format(self.id)


class Article(Base):
    STATUSES = (
        (0, 'Draft'),
        (1, 'Published'),
        (2, 'Deleted')
    )

    title = models.CharField(max_length=70, unique=True)
    slug = models.SlugField(max_length=70, unique=True)
    content = models.TextField(max_length=23256)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUSES, default=0)

    def __str__(self):
        return '<Article: ID - {id}>'.format(self.id)
