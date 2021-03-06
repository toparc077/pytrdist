from django.conf.urls import patterns, include, url
from django.conf import settings
from trwk.views import trwk_home
from trwk.sitemap import (
    PostSitemap, DocumentSitemap, SeminarSitemap, CompanySitemap
)
from django.contrib.sitemaps.views import sitemap
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps import FlatPageSitemap

sitemaps = {
    'post': PostSitemap,
    'document': DocumentSitemap,
    'seminar': SeminarSitemap,
    'company': CompanySitemap,
    'flatpage': FlatPageSitemap,
}

urlpatterns = patterns(
    '',
    url(r'^$',          trwk_home, name='home'),
    url(r'^accounts/',  include('registration.backends.default.urls')),
    url(r'^accounts/',  include('accounts.urls')),
    url(r'^company/',   include('accounts.company_urls')),
    url(r'^mypage/',    include('mypage.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^seminars/',  include('seminars.urls')),
    url(r'^contact/',   include('contact.urls')),
    url(r'^search/',    include('search.urls')),
    url(r'^blog/',      include('blog.urls')),
    url(r'^pages/',     include('django.contrib.flatpages.urls')),
    (r'^sitemap\.xml$',
        cache_page(21600)(sitemap),
        {'sitemaps': sitemaps}),
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    )
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    )

if settings.ADMIN:
    from django.contrib import admin
    admin.autodiscover()
    urlpatterns += patterns(
        '',
        url(r'^admin/',      include(admin.site.urls)),
        url(r'^operations/', include('operations.urls')),
    )


from django.template import add_to_builtins
add_to_builtins('django.contrib.humanize.templatetags.humanize')
add_to_builtins('trwk.templatetags.site_extra')
