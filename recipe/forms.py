from django import forms
from recipe.models import Recipe, Comment


# Custom widget for integrating Summernote WYSIWYG editor into forms
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


# Form for creating or updating Recipe instances
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


# Form for creating comments on Recipe instances
class CommentForm(forms.ModelForm):
    """
    Form for creating comments on Recipe instances.
    """
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={
                    'class': 'form-control mt-3',
                    'id': 'comment',
                    'name': 'comment',
                    'rows': 5,
                    'placeholder': 'Add a comment...'
                }
            ),
        }
