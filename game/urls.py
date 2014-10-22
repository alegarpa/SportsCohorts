from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'game.views.index', name='index'), #remove this later

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^(?P<gamename>\d+)/$', 'game.views.getGamePage'),
	#url(r'^create', 'game.views.create', name='create'),
	#url(r'^addPlayer', 'game.views.addPlayer', name='addPlayer'),
	#url(r'^removePlayer', 'game.views.removePlayer', name='removePlayer'),
	#url(r'^invite', 'game.views.invite', name='invite'),
	#url(r'^timeChange', 'game.views.timeChange', name='timeChange'),
	#url(r'^locationChange', 'game.views.locationChange', name='locationChange'),

]