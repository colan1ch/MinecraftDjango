from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm
from .models import *


CHOICES_GAMEMODE = (
    ("creative", "creative"),
    ("survival", "survival"),
    ("adventure", "adventure"),
    ("spectator", "spectator"),
)
CHOICES_DIFFICULTY = (
    ("peaceful", "peaceful"),
    ("easy", "easy"),
    ("normal", "normal"),
    ("hard", "hard"),
)


class SetServerSettingsForm(forms.Form):
    max_players = forms.CharField(label='max_players', initial='20')
    gamemode = forms.ChoiceField(
        label='gamemode', choices=CHOICES_GAMEMODE, initial='survival')
    difficulty = forms.ChoiceField(
        label='difficulty', choices=CHOICES_DIFFICULTY, initial='normal')
    white_list = forms.BooleanField(
        label='white_list', initial=False, required=False)
    online_mode = forms.BooleanField(
        label='online_mode', initial=False, required=False)
    pvp = forms.BooleanField(
        label='pvp', initial=True, required=False)
    allow_flight = forms.BooleanField(
        label='allow_flight', initial=True, required=False)
    spawn_animals = forms.BooleanField(
        label='spawn_animals', initial=True, required=False)
    spawn_monsters = forms.BooleanField(
        label='spawn_monsters', initial=True, required=False)
    spawn_npcs = forms.BooleanField(
        label='spawn_npcs', initial=True, required=False)
    allow_nether = forms.BooleanField(
        label='allow_nether', initial=True, required=False)
    enable_command_block = forms.BooleanField(
        label='command_block', initial=True, required=False)
