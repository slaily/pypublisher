from django.template import (
    Context,
    Engine,
    TemplateDoesNotExist,
    loader
)

from project.apps.base import constants


def load_page_not_found_template(request):
    """
    Loads content of page not found template.

    Template: `base/404.html`

    :return:
        Returns a :class:`django.utils.safestring.SafeText`
        used for “safe” HTML output purposes.
    """
    try:
        template = loader.get_template(constants.ERROR_404_TEMPLATE_PATH)
        content = template.render(request=request)
    except TemplateDoesNotExist:
        template = Engine().from_string(
            '<h1>Not Found</h1>'
            '<p>The requested URL was not found on this server.</p>'
        )
        content = template.render(Context({}))

    return content
