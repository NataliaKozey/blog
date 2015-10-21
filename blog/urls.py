from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',


    url(r'^', include('my_blog.urls')),
    url(r'^auth/', include('loginsys.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
