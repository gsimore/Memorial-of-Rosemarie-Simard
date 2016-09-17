from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'name', 'image', 'has_image')
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Tell your stories, memories and prayers here.', 'class': 'form-text'}),
        }
