from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from musicapp.models import Artist, Song
from musicapp.forms import ArtistForm, SongForm
from django.urls import reverse_lazy


class LandingPageView(TemplateView):
    template_name = 'home.html'

class ArtistListView(ListView):
    model= Artist 
    context_object_name= 'artists'
    template_name= 'list_artist.html'


class ArtistCreateView(CreateView):
  model = 'Artist'
  form_class = ArtistForm
  template_name = 'add_artist.html'
  success_url = reverse_lazy('artists')

class ArtistUpdateView(UpdateView):
  model = Artist
  form_class = ArtistForm
  template_name = 'edit_artist.html'
  success_url = reverse_lazy('artists')


def deleteArtist(request, pk):
  artist = Artist.objects.get(id=pk)
  artist.delete()
  return redirect('/artists')


class ArtistCreateSongView(CreateView):
  model = 'Song'
  form_class = SongForm
  template_name = 'add_song.html'
  success_url = reverse_lazy('songs')


class SongUpdateView(UpdateView):
  model = 'Song'
  form_class = ArtistForm
  template_name = 'edit_artist.html'
  success_url = reverse_lazy('artists')


class SongListView(ListView):
  model= Song
  context_object_name= 'songs'
  template_name= 'list_song.html'
    