from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from LoginCounter.views import client, login, add, resetFixture, unitTests
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', client),
	(r'^users/login$', login),
	(r'^users/add$', add),
	(r'^TESTAPI/resetFixture$', resetFixture),
	(r'^TESTAPI/unitTests$', unitTests),
    #(r'^(?P<path>.*js)$', 'django.views.static.serve', {'document_root':os.path.dirname(os.path.abspath(__file__)) + '/templates/'}),
    #(r'^(?P<path>.*css)$', 'django.views.static.serve', {'document_root':os.path.dirname(os.path.abspath(__file__)) + '/templates/'}),
    
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^backend/', include('backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('', (r'^(?P<path>.*js)$', 'django.views.static.serve', {'document_root':os.path.dirname(os.path.abspath(__file__)) + '/templates/'}),)
urlpatterns += patterns('', (r'^(?P<path>.*css)$', 'django.views.static.serve', {'document_root':os.path.dirname(os.path.abspath(__file__)) + '/templates/'}),)
#urlpatterns += staticfiles_urlpatterns()