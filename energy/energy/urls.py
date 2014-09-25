from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^reviews/', include('reviews.urls', namespace='reviews')),
    url(r'^admin/', include(admin.site.urls)),
)
