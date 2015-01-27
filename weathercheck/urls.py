from django.conf.urls import patterns, url

from weathercheck import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
