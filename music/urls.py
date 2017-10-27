from django.conf.urls import patterns, url
from music import views

# urlpatterns = [
#     url(r'^$', views.index,name='index'),
# ]

urlpatterns = [
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^$', views.music_list, name='music_list'),
    url(r'^album/$', views.album_list, name='album_list'),
    url(r'^album/new$', views.album_create, name='album_new'),
    url(r'^album/edit/(?P<pk>\d+)$', views.album_update, name='album_edit'),
    url(r'^album/delete/(?P<pk>\d+)$', views.album_delete, name='album_delete'),

    url(r'^song/(?P<pk>[0-9]+)/$', views.song_detail, name='song_detail'),
    url(r'^song/$', views.song_list, name='song_list'),
    url(r'^song/new$', views.song_create, name='song_new'),
    url(r'^song/edit/(?P<pk>\d+)$', views.song_update, name='song_edit'),
    url(r'^song/delete/(?P<pk>\d+)$', views.song_delete, name='song_delete'),
]
