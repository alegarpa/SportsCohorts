from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'sport.views.index', name='index'), #remove this later
    url(r'^all', 'sport.views.viewAllSports', name='viewAllSports'),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^sports/(?P<sportname>\d+)/$', 'sport.views.showCalendar'),
	#url(r'^sport/addGame', 'sport.views.addGame', name='addGame'),
	# not for iteration 1:  url(r'^sport/addSport', 'sport.views.addSport', name='addSport'),


	]