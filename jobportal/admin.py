from django.contrib import admin

# Register your models here.
from .models import JobSeeker, Employer, Job, JobApplication

admin.site.register(JobSeeker)
admin.site.register(Employer)
admin.site.register(Job)
admin.site.register(JobApplication)
