from django import forms
from .models import Movie, Comment


class CommentForm(forms.Form):
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={'placeholder': 'Your Comment'}))