from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    from_email = forms.EmailField(max_length=254)
    subject = forms.CharField(max_length=128)
    message = forms.CharField(max_length=2512, widget=forms.Textarea)

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
