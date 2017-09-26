from django.db import models
from django.core.urlresolvers import reverse


class Application(models.Model):
    name = models.CharField(max_length=200)
    technology = models.CharField(max_length=200)
    description = models.TextField()
    status_options = (('select', 'Select'),('Accept', 'Accept'),('Reject', 'Reject'))
    status = models.CharField(max_length=20, choices=status_options, default='select', verbose_name="Application Status",)

    def __str__(self):
   		return self.name