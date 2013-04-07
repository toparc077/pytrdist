from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trwk.views.home', name='home'),
    # url(r'^trwk/', include('trwk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/',             include(admin.site.urls)),
    url(r'^accounts/',          include('registration.backends.default.urls')),
    url(r'^accounts/password/', include('password_reset.urls')),
)
