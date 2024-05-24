from django import forms
from cloudinary.forms import CloudinaryFileField
from recipe.models import Recipe

class RecipeForm(forms.ModelForm):
    photo = CloudinaryFileField()

    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'steps', 'photo', 'tags', 'is_public']
        widgets = {
            'ingredients': forms.Textarea(attrs={'rows': 4}),
            'steps': forms.Textarea(attrs={'rows': 4}),
        }
