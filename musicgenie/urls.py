
from django.contrib import admin
from django.urls import path
from music_app.view import LandingPageView, ArtistCreateView, ArtistListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',LandingPageView.as_view(), name='home'),
    path('artists', ArtistListView.as_view(),name='artists'),
    path('add_artist',ArtistCreateView.as_view(),name='add_artist'),
    


]
