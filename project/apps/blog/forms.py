from django import forms
from django.core.mail import send_mail


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

        send_mail(
            subject,
            message,
            from_email,
            ['to@test.com'],
            fail_silently=False,
        )

        return None
