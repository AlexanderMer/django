# This file was created by me to keep things organsied, it is imported in
# the awesome_armadillo/urls.py

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #/music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # (?P<pk>[0-9]+) gets the pk integer
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),
]