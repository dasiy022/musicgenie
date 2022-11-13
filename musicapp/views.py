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
    template_name= 'list_artists.html'

