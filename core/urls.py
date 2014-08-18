from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tips.core.views',
    url(r'^$', 'home', name='home'),

    url(r'^api/tags/$', 'get_tags'),
    url(r'^api/tips/$', 'get_tips'),

)
