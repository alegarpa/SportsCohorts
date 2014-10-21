from django.conf.urls import patterns, include, url
from django.contrib import admin

from messagePost import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
	#url(r'^messagePost/addPost', 'messagePost.views.addPost', name='addPost'),
	#url(r'^messagePost/deletePost', 'messagePost.views.deletePost', name='deletePost'),

]