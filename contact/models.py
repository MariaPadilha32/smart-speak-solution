from django.db import models

# models below


class Contact(models.Model):
    """Model for contact form"""
    CONTACT_CHOICES = [
        ('general', 'General Query'),
        ('order', 'Order Tracking'),
        ('return', 'Return Request'),
        ('complaint', 'Complaint'),
    ]
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField(max_length=700)
    #reason = models.CharField(max_length=15, choices=CONTACT_CHOICES)

    def __str__(self):
        return self.email
