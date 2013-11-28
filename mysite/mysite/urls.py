from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from mysite.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^hello/$', hello),
    ('^time/$', current_datetime),
    (r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
)
