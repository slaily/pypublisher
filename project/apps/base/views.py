from django.views.generic.base import TemplateView
from django.http import HttpResponseNotFound

from project.apps.base import helpers


def page_not_found(request, exception):
    """
    404 handler.

    :return:
        Returns a :class:`HttpResponseNotFound` with 404 status code
    """
    content = helpers.load_page_not_found_template(request)

    return HttpResponseNotFound(content)


class IndexView(TemplateView):
    template_name = 'base/index.html'
