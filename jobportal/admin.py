from django.contrib import admin

# Register your models here.
from .models import User, Company, Job, JobApplication

admin.site.register(User)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobApplication)
