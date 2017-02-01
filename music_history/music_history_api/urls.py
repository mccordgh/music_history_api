from django.conf.urls import url, include
from rest_framework import routers
from music_history.music_history_api import views

router = routers.DefaultRouter()
router.register(r'artists', views.ArtistView)
router.register(r'albums', views.AlbumView)
router.register(r'songs', views.SongView)
router.register(r'genres', views.GenreView)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]