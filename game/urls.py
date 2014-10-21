from django.conf.urls import patterns, include, url
from django.contrib import admin

from game import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^game/(?P<gamename>\d+)/$', 'game.views.getGamePage'),
	#url(r'^game/create', 'game.views.create', name='create'),
	#url(r'^game/addPlayer', 'game.views.addPlayer', name='addPlayer'),
	#url(r'^game/removePlayer', 'game.views.removePlayer', name='removePlayer'),
	#url(r'^game/invite', 'game.views.invite', name='invite'),
	#url(r'^game/timeChange', 'game.views.timeChange', name='timeChange'),
	#url(r'^game/locationChange', 'game.views.locationChange', name='locationChange'),

]