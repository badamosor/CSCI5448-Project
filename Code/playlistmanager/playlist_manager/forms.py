from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

from .models import Playlist

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class PlaylistForm(ModelForm):
    playlist_name = forms.CharField()
    playlist_description = forms.CharField()
    class Meta:
        model = Playlist
        fields = ('playlist_name', 'playlist_description')
