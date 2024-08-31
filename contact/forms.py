from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         placeholders = {
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
            'reason': 'Reason for contact',
        }

         self.fields['email'].widget.attrs['autofocus'] = True

class ContactGeneralForm(ModelForm):
    class Meta:
        model = Contact
        fields = ("email", "subject", "message")

    def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         placeholders = {
            'email': 'Email',
            'subject' : 'Subject',
            'message': 'Message',
            
        }

         self.fields['email'].widget.attrs['autofocus'] = True