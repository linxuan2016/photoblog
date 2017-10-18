# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.views.generic.base import RedirectView
#from blog.views import blog_home

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
]

urlpatterns += i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^blog/', include('blog.urls')),
    url(r'^gallery/', include('gallery.urls')),
    #url(r'^$', RedirectView.as_view(url='/blog/home/')),
    url(r'^', include('cms.urls')),
    url(r'^', include('django_login.urls')),
)

urlpatterns +=[
    url(r'^comments/', include('django_comments.urls')),
    url(r'^filer/', include('filer.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns
