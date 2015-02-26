from django.conf.urls import patterns, include, url
from django.contrib import admin

from .views import home
from .api import get_search, get_user

urlpatterns = patterns('',
                       url(r'^$', home, name='app_home'),
                       url(r'^user/(?P<username>\w{0,50})/$', get_user, name='app_get_user'),
                       url(r'^buscar/(?P<query>\w{0,50})/', get_search, name='app_get_search'),
)
