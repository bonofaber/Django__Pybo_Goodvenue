from django import forms
from django.forms import ModelForm
from articleapp.models import Article

class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-start',
                                                           'style': 'height: auto;'}))
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']