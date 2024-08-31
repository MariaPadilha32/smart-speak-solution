from django.db import models

# models below


class Contact(models.Model):
    """Model for contact form"""
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=700)

    def __str__(self):
        return self.email
