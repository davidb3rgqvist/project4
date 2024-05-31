from django import forms
from recipe.models import Recipe, Comment

class SimpleSummernoteWidget(forms.Textarea):
    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-bs4.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/summernote/0.8.18/summernote-bs4.min.js',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['class'] = 'form-control simple-summernote'

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'ingredients', 'steps', 'photo', 'is_public']
        widgets = {
            'description': SimpleSummernoteWidget(),
            'steps': SimpleSummernoteWidget(),
            'ingredients': SimpleSummernoteWidget(),
        }

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ['text']
        labels = {
            'text': ''
        }
