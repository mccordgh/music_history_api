from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from music_history_api.views import *

router = routers.DefaultRouter()
router.register(r'artists', artist_view.ArtistView)
router.register(r'albums', album_view.AlbumView)
router.register(r'songs', song_view.SongView)
router.register(r'genres', genre_view.GenreView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]