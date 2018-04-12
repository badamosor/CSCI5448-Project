from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Playlist

class UserForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    class MetaUser:
        model = User
        fields = ('username', 'email', 'password')
class PlaylistForm(forms.Form):
    playlist_name = forms.CharField()
    playlist_description = forms.CharField()
    collaborative_status = forms.BooleanField(initial = False, required = False)
    class MetaPlaylist:
        model = Playlist
        fields = ('playlist_name', 'playlist_description', 'collaborative_status')
