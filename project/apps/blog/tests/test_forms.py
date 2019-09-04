from unittest import TestCase

from django.core import mail

from project.apps.blog import forms


class ContactFormTest(TestCase):
    def test_send_email(self):
        form = forms.ContactForm(
            data={
                'subject': 'Test Subject',
                'message': 'Test Message',
                'from_email': 'test@test.com'
            }
        )
        form.is_valid()

        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
