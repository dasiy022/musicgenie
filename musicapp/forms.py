from django import forms

from .models import Artist, Song
from crispy_forms.helper import FormHelper 

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields= ('name', 'age', 'nationality', 'website', 'height', 'label', 'image_url')

        def _init_(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.helper= FormHelper ()
            self.helper.form_method = 'POST'

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields=('title', 'genre', 'release_date', 'artist')

        def _init_(self, *args, **kwargs):
            super().__init__ (*args, **kwargs)
            self.helper = FormHelper()
            self.helper.from_method = 'POST'
            self.helper.render_required_fields = False
