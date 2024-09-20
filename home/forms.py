from django import forms


class NewsletterForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    recipients = forms.CharField(help_text='Comma-separated email addresses')

    def clean_recipients(self):
        emails = self.cleaned_data['recipients']
        emails_list = [email.strip() for email in emails.split(',')]
        return emails_list