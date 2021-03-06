from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

#import datetime

from datetime import datetime

from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    #name = models.CharField(max_length=200)
    # location
    #join_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('jobportal:apply', kwargs={'pk': self.pk})

@python_2_unicode_compatible
class Company(models.Model):
    name = models.CharField(max_length=200)
    join_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Resume(models.Model):
    resume_file = models.FileField()
    owner = models.ForeignKey(Person, default=1)
    #user = models.ForeignKey(User, default=1)
    pub_date = models.DateTimeField('date published')
    name = models.CharField(max_length=200)#, blank=True, null=True)

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Job(models.Model):
    name = models.CharField(max_length=200)

    #title = models.CharField(max_length=200)
    #pub_date = models.DateTimeField('date posted')

    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    #def get_absolute_url(self):
    #    return reverse('jobportal:apply', kwargs={'pk': self.pk})

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
