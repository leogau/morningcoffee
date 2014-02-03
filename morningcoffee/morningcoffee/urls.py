from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

import app

urlpatterns = patterns('',
    url(r'^$', 'app.views.index', name='index'),
    # url(r'^summarize/$', ' app.views.summarize', name='summarize'),
    url(r'^summarize/(?P<url>.*)/$', 'app.views.summarize', name='summarize'),
)
