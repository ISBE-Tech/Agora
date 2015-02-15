from django.conf.urls import patterns, include, url
from views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'agora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', display_page),
    url(r'^name-enter/$', get_name),
    url(r'^create-post/$', create_post)
)