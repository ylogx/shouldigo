from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'shouldigo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^weathercheck/', include('weathercheck.urls')),
    url(r'^$', include('weathercheck.urls')),   #XXX: Points to weathercheck
    url(r'^googleeac30150b558f9bc\.html$', RedirectView.as_view(url='/static/googleeac30150b558f9bc.html'))
)
