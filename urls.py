"""This is the root url configuration file"""

from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import include
from django.conf.urls.defaults import url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^exam/', include('The_Xaming_Arena.exam.urls')),
    url(r'^accounts/profile/', 'The_Xaming_Arena.exam.views.home',
        {'template_name': 'accounts/home.html'}),
)
