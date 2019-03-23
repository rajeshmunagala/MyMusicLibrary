from django.urls import path, re_path
from . import views

app_name = 'music'
urlpatterns = [
    # /music/
    path('', views.IndexView.as_view(), name='index'),
    path('register', views.UserFormView.as_view(), name='register'),
    # /music/<album_id>/
    re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add
    re_path(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

# /music/album/2
    re_path(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),

# /music/album/2/delete
    re_path(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),

    # / music / < album_id >/favorite/
#    re_path(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),
]