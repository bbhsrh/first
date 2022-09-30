from django import forms
from .models import Post

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    
class TownSearchForm(forms.Form):
    search_town = forms.ChoiceField(label='Search Town', choices=Post.town_choices)