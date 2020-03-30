from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import (
    path,
    include
)

from project.apps.blog.sitemaps import (
    ArticleSitemap,
    StaticViewSitemap
)


sitemaps = {
    'articles': ArticleSitemap,
    'contact': StaticViewSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.apps.base.urls')),
    path('blog/', include('project.apps.blog.urls')),
    path(
        'sitemap.xml',
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap'
    )
]

handler404 = 'project.apps.base.views.page_not_found'
