from django import forms
from django.forms import inlineformset_factory
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget
from recipe.models import Recipe, Comment


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'photo', 'is_public']
        widgets = {
            'description': SummernoteWidget(),
            'steps': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': '' 
        }