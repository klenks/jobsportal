from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'jobportal'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index')
    url(r'^$', views.index, name='index'),
    url(r'^/employer/(?P<employer_id>[0-9]+)/$', views.employer, name='employer'),
    url(r'^/job/(?P<job_id>[0-9]+)/$', views.job, name='job')
]
