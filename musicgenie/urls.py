
from django.contrib import admin
from django.urls import path
from musicapp.views import ArtistListView,LandingPageView, ArtistCreateView, ArtistUpdateView, deleteArtist, ArtistCreateSongView,SongUpdateView, SongListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',LandingPageView.as_view(), name='home'),
    path('artists', ArtistListView.as_view(),name='artists'),
    path('add_artist',ArtistCreateView.as_view(),name='add_artist'),
    path('artist-details/<int:pk>', ArtistUpdateView.as_view(),name='artist_details'),
    path('artist-delete/<int:pk>', deleteArtist,name='delete_artist'),
    path('add_song', ArtistCreateSongView.as_view(),name='add_song'),
    path('edit_artist',ArtistUpdateView.as_view(),name='edit_artist'),
    path('edit_song', SongUpdateView.as_view(),name='edit_song'),
    path('songs', SongListView.as_view(),name='songs')  
]
