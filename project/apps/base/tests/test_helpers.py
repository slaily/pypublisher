from unittest import TestCase
from unittest.mock import patch

from project.apps.base import helpers


class LoadPageNotFoundTemplateTest(TestCase):
    def test_load_page_not_found_template(self):
        content = helpers.load_page_not_found_template({})

        self.assertEqual(content, '<h1>404 - Not Found</h1>\n')

    @patch(
        'project.apps.base.helpers.constants.ERROR_404_TEMPLATE_NAME',
        'base/wrong_404'
    )
    def test_load_page_not_found_template_with_not_existing_template(self):
        content = helpers.load_page_not_found_template({})

        self.assertNotEqual(content, '<h1>404 - Not Found</h1>\n')

    def test_new_pass(self):
        pass
