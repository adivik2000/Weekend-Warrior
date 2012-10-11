from django.conf.urls import patterns, include, url
from restaurants.views import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'warrior.views.home', name='home'),
    url(r'^$', direct_to_template, {'template': 'land.html'}),
    url(r'^chennai/', home),
    url(r'^bangalore/', bangalore),
    url(r'^delhi/', delhi),
    url(r'^mumbai/', mumbai),
    # url(r'^warrior/', include('warrior.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )