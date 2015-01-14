from django.conf.urls import patterns, include, url
from django.contrib import admin
import staff
# from xadmin.plugins import xversion
# Uncomment the next two lines to enable the admin:

admin.autodiscover()


# xversion.registe_models()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'officeos.views.home', name='home'),
    # url(r'^officeos/', include('officeos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^staff/', include('staff.urls', namespace='staff'))

)
