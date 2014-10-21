from django.conf.urls import patterns, include, url
from django.contrib import admin

from sport import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


    url(r'^admin/', include(admin.site.urls)),
    #url(r'^sports', 'sport.views.viewAllSports', name='viewAllSports'),
    #url(r'^sports/(?P<sportname>\d+)/$', 'sport.views.showCalendar'),
	#url(r'^sport/addGame', 'sport.views.addGame', name='addGame'),
	# not for iteration 1:  url(r'^sport/addSport', 'sport.views.addSport', name='addSport'),


	]