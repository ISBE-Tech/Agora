from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from board import views

urlpatterns = patterns('board.views',
    # Examples:
    # url(r'^$', 'agora.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
   	url('^$', views.index),
)