from django.conf.urls import patterns, url

from upload import views

urlpatterns = patterns('',
    url(r'^$', views.upload_view, name='upload_view'),
    )
