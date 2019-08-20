from django.test import SimpleTestCase


class PageNotFoundViewTest(SimpleTestCase):
    def test_page_not_found(self):
        response = self.client.get('/404')

        self.assertEqual(response.status_code, 404)
