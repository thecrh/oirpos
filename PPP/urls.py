from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from Forum.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PPP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'Forum.views.forum'),
    # /topic/{id}
    url(r'^topic/(?P<topic_id>\d+)/$', 'Forum.views.topic'),
    # /topic/new
    url(r'^topic/new/$', 'Forum.views.new', name='TopicForm'),
    # /topic/{id}/reply/
    url(r'^topic/(?P<topic_id>\d+)/reply/$', 'Forum.views.reply', name='ReplyForm'),
)
