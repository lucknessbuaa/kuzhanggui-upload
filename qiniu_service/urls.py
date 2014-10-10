from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qiniu_service.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^upload/', include('upload.urls', namespace='upload')),
    url(r'^qiniu_upload/', include('upload.urls', namespace='upload')),

)
