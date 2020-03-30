from django import forms
from django.core.mail import send_mail
from django.conf import settings

from project.apps.blog.constants import EMAIL_TEMPLATE_STR


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        label='',
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email *'
            }
        )
    )
    subject = forms.CharField(
        label='',
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Subject *'
            }
        )
    )
    message = forms.CharField(
        label='',
        max_length=2512,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Message *'
            }
        )
    )

    def send_email(self):
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        from_email = self.cleaned_data['from_email']
        formatted_message = EMAIL_TEMPLATE_STR.format(
            email=from_email,
            subject=subject,
            message=message
        )
        send_mail(
            subject,
            formatted_message,
            'to@test.com',
            [settings.DEFAULT_FROM_EMAIL],
            fail_silently=False,
        )

        return None
