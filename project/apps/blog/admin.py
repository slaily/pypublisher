from django.contrib import admin

from project.apps.blog import models


admin.site.register(
    [
        models.Author,
        models.Article
    ],
)
