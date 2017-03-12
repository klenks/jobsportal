from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

#import datetime

from datetime import datetime

from django.utils import timezone

# Create your models here.
@python_2_unicode_compatible
class JobSeeker(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Employer(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Job(models.Model):
    name = models.CharField(max_length=200)
    #title = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date posted')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    def get_absolute_url(self):
        return reverse('jobportal:apply', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class JobApplication(models.Model):
    name = models.CharField(max_length=200)
    cover_letter = models.CharField(max_length=200)
    #title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
