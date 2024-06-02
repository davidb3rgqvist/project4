from django import forms  # Importing the forms module
from recipe.models import Recipe, Comment  # Importing models

class SimpleSummernoteWidget(forms.Textarea):
    """
    Custom widget for integrating Summernote WYSIWYG editor into forms.
    """
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-bs4.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-bs4.min.js',)

    def __init__(self, *args, **kwargs):
        """
        Initializes the widget and sets its attributes.
        """
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control simple-summernote'

class RecipeForm(forms.ModelForm):
    """
    Form for creating or updating Recipe instances.
    """
    class Meta:
        """
        Meta class specifying the model and fields to include in the form.
        """
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'photo', 'is_public']
        widgets = {
            'description': SimpleSummernoteWidget(),
            'steps': SimpleSummernoteWidget(),
            'ingredients': SimpleSummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    """
    Form for creating comments on Recipe instances.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the form and sets additional attributes.
        """
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'form-control'

    class Meta:
        """
        Meta class specifying the model and fields to include in the form.
        """
        model = Comment
        fields = ['text']
        labels = {
            'text': ''  # Hides label for the 'text' field
        }
