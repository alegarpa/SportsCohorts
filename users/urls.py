from django.conf.urls import patterns, include, url
from django.contrib import admin

from users import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^user/(?P<username>\d+)/$', 'user.views.getUserPage', name='getUserPage'),
    #url(r'^user/myprofile', 'user.views.getSelfProfile', name='getSelfProfile'),
    #url(r'^user/register', 'user.views.register', name='register'),
    #url(r'^user/login', 'user.views.login', name='login'),
	#url(r'^user/requestFriend', 'user.views.requestFriend', name='requestFriend'),
	#url(r'^user/confirmFriendRequest', 'user.views.confirmFriendRequest', name='confirmFriendRequest'),
	#url(r'^user/rejectFriendRequest', 'user.views.rejectFriendRequest', name='rejectFriendRequest'),
	#url(r'^user/removeFriend', 'user.views.removeFriend', name='removeFriend'),
	#url(r'^user/joinGame', 'user.views.joinGame', name='joinGame'),
	#url(r'^user/unjoinGame', 'user.views.unjoinGame', name='unjoinGame'),
	#url(r'^user/changeIcon', 'user.views.changeIcon', name='changeIcon'),
	
]