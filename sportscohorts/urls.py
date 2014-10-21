from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SportsCohorts2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'users.views.home', name='home'),
    
	url(r'^game/', include('game.urls')),
	url(r'^sport/', include('sport.urls')),
	url(r'^users/', include('users.urls')),
	url(r'^messagePost/', include('messagePost.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
