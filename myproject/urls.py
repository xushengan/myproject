from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'boards.views.home', name='home'),
    url(r'^boards/(?P<pk>\d+)/$','boards.views.board_topics',name='board_topics'),
    url(r'^admin/', include(admin.site.urls)),
)
