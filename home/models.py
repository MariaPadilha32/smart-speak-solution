from django.db import models
from django.utils import timezone


class Newsletter(models.Model):

    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    subscribed = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Newsletter subscribers'
        ordering = ['created']

    def __str__(self):
        return self.name


class SubscribedUsers(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    class Meta:
        db_table = 'SubscribedUsers'

    def __str__(self):
        return self.email
