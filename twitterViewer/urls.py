from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'twitterViewer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', 'app.views.home',name='app_home'),
    url(r'^api/user/(?P<username>\w{0,50})/$', 'api.views.get_user',name='api_get_user'),
    url(r'^api/buscar/(?P<query>\w{0,50})/', 'api.views.get_search',name='api_get_search'),
)
