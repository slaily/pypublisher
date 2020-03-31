from unittest import TestCase
from unittest.mock import patch

from project.apps.base import helpers


class LoadPageNotFoundTemplateTest(TestCase):
    @patch(
        'project.apps.base.helpers.constants.ERROR_404_TEMPLATE_PATH',
        'base/wront_404.html'
    )
    def test_load_page_not_found_template_with_not_existing_template(self):
        content = helpers.load_page_not_found_template({})

        self.assertNotEqual(content, '<h1>404</h1>\n')
