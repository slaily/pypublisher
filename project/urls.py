from django.contrib import admin
from django.urls import (
    path,
    include
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('project.apps.base.urls')),
    path('blog/', include('project.apps.blog.urls')),
]
