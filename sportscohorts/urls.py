from django.conf.urls import patterns, include, url
from django.contrib import admin
from users import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sportscohorts.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/register', views.register),
    url(r'^user/login', views.login),
    url(r'^user/logout', views.logout),
    url(r'^user/requestFriend', views.requestFriend),
    url(r'^TESTAPI/reset', views.reset),
    
)
