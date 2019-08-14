from django.views.generic.base import TemplateView
from django.http import HttpResponseNotFound
from django.template import (
    Context,
    Engine,
    TemplateDoesNotExist,
    loader
)


ERROR_404_TEMPLATE_NAME = 'base/404.html'


def page_not_found(request, exception):
    """
    404 handler.

    Template: `base/404.html`
    """
    try:
        template = loader.get_template(ERROR_404_TEMPLATE_NAME)
        body = template.render(request=request)
    except TemplateDoesNotExist:
        template = Engine().from_string(
            '<h1>Not Found</h1>'
            '<p>The requested URL was not found on this server.</p>'
        )
        body = template.render(Context({}))
    return HttpResponseNotFound(body)


class IndexView(TemplateView):
    template_name = 'base/index.html'
