from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = [
    url(r'^$', 'users.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^all', 'users.views.viewAllPlayers', name='viewAllPlayers'),

    # this takes you to any user's profile
    # right now just testing that template works; will change this to work for all users later
    url(r'^test', 'users.views.getUserPage', name='getUserPage'),

    url(r'^myprofile', 'users.views.getSelfProfile', name='getSelfProfile'),
    url(r'^mygames', 'users.views.getSelfGames', name='getSelfGames'),
    #url(r'^users/register', 'users.views.register', name='register'),
    #url(r'^users/login', 'users.views.login', name='login'),
	#url(r'^users/requestFriend', 'users.views.requestFriend', name='requestFriend'),
	#url(r'^users/confirmFriendRequest', 'users.views.confirmFriendRequest', name='confirmFriendRequest'),
	#url(r'^users/rejectFriendRequest', 'users.views.rejectFriendRequest', name='rejectFriendRequest'),
	#url(r'^users/removeFriend', 'users.views.removeFriend', name='removeFriend'),
	#url(r'^users/joinGame', 'users.views.joinGame', name='joinGame'),
	#url(r'^users/unjoinGame', 'users.views.unjoinGame', name='unjoinGame'),
	#url(r'^users/changeIcon', 'users.views.changeIcon', name='changeIcon'),
	
]