from django.conf.urls import patterns, include, url
from django.contrib import admin
import staff
import xadmin


xadmin.autodiscover()
admin.autodiscover()
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = patterns('',
    url(r'xadmin/', include(xadmin.site.urls)),
    url(r'^staff/', include('staff.urls', namespace='staff')),
    url(r'^admin/', include(admin.site.urls)),
)
#
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'officeos.views.home', name='home'),
#     # url(r'^officeos/', include('officeos.foo.urls')),
#
#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
#
#     # Uncomment the next line to enable the admin:
#
#
# )
