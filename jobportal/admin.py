from django.contrib import admin

# Register your models here.
from .models import Person, Company, Job, JobApplication, Resume

admin.site.register(Person)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobApplication)
admin.site.register(Resume)
