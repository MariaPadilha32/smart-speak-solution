from django import forms


class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    receivers = forms.CharField(
        widget=forms.Textarea,
        help_text='Comma-separated email addresses'  # Add receivers field
    )

    def clean_recipients(self):
        emails = self.cleaned_data['receivers']
        emails_list = [email.strip() for email in emails.split(',')]
        return emails_list
