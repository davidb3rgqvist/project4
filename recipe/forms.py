from django import forms
from django.forms import inlineformset_factory
from cloudinary.forms import CloudinaryFileField
from django_summernote.widgets import SummernoteWidget
from recipe.models import Recipe
# from .models import Photo


# class IngredientForm(forms.ModelForm):
#     class Meta:
#         model = Ingredient
#         fields = ['name', 'quantity']


# IngredientFormSet = inlineformset_factory(Recipe, Ingredient, form=IngredientForm, extra=1)


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'photo', 'tags', 'is_public']
        widgets = {
            'description': SummernoteWidget(),
            'steps': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
        }
