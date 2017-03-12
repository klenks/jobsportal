from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'jobportal'
urlpatterns = [

    #url(r'^$', views.IndexView.as_view(), name='index')

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^employer/(?P<employer_id>[0-9]+)/$', views.employer, name='employer'),

    #url(r'^/job/(?P<job_id>[0-9]+)/$', views.job, name='job')

    url(r'^job/(?P<pk>[0-9]+)/$', views.JobView.as_view(), name='job'),

    #url(r'job/add/$', views.JobCreate.as_view(), name='job-add')

    url(r'job/add/$', views.JobFormView.as_view(), name='job-add')
]
