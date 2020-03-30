from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from project.apps.blog.models import Article


class ArticleSitemap(Sitemap):
    changefreq = "monthly"
    priority = 1.0
    protocol = 'https'

    def items(self):
        return Article.objects.filter(status=1)

    def location(self, item):
        return reverse(
            'blog-article-detail-view',
            args=[item.slug]
        )


class StaticViewSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5
    protocol = 'https'

    def items(self):
        return ['blog-contact-view']

    def location(self, item):
        return reverse(item)
