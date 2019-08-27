from unittest import TestCase

from django.test import SimpleTestCase

from project.apps.blog.views import ContactView


class PageNotFoundViewTest(SimpleTestCase):
    def test_page_not_found(self):
        response = self.client.get('/404')

        self.assertEqual(response.status_code, 404)


class ContactViewTest(TestCase):
    def test_form_valid(self):
        contact_view = ContactView()
        contact_form = contact_view.form_class(
         data={
                'subject': 'Test Subject',
                'message': 'Test Message',
                'from_email': 'test@test.com'
            }
        )
        contact_form.is_valid()
        response = contact_view.form_valid(contact_form)

        self.assertEqual(response.status_code, 302)
