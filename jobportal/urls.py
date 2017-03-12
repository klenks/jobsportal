from django.conf.urls import include, url
from django.contrib import admin

from . import views

app_name = 'jobportal'
urlpatterns = [
    #url(r'^$', views.IndexView.as_view(), name='index')
    url(r'^$', views.index, name='index')
]
