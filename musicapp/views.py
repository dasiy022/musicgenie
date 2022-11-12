from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, listView, CreateView, UpdateView, 
from music_app.models import Artist, Song
from music_app.forms import ArtistForm, SongForm
from django.urls import reverse_lazy


class LandingPageView(TemplateView):
    template_name = 'home.html'

class ArtistListView(ListView):
    model= Artist 
    context_object_name= 'artists'
    template_name= 'list_artists.html'

