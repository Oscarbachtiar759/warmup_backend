from django.conf.urls import patterns, include, url
from LoginCounter.views import login, add, resetFixture, unitTests

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	(r'^users/login$', login),
	(r'^users/add$', add),
	(r'^TESTAPI/resetFixture$', resetFixture),
	(r'^TESTAPI/unitTests$', unitTests),
    # Examples:
    # url(r'^$', 'backend.views.home', name='home'),
    # url(r'^backend/', include('backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
