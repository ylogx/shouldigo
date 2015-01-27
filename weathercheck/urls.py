from django.conf.urls import patterns, url

from weathercheck import views

urlpatterns = patterns('',
    url(r'^$', views.today, name='today'),
    #url(r'^$', views.index, name='index'),
    url(r'today/', views.today, name='today'),
)
