from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^app/', include('app.url')),
                       (r'^accounts/', include('userena.urls')),
)
