from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'boards.views.home', name='home'),
    url(r'signup/$','accounts.views.signup',name='signup'),
    url(r'^boards/(?P<pk>\d+)/$','boards.views.board_topics',name='board_topics'),
    url(r'^boards/(?P<pk>\d+)/new/$','boards.views.new_topic',name='new_topic'),
    url(r'^admin/', include(admin.site.urls)),
)
