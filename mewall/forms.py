from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'name', 'image', 'description', 'has_image')
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': 'Tell your stories, memories and prayers here.', 'class': 'form-text'}),
            'description': forms.TextInput(attrs={'placeholder': 'Write a brief description of your image.', 'class': 'form-description'}),
        }

    def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['title'].label = "Title"
            self.fields['text'].label = "Your words:"
            self.fields['name'].label = "Your name:"
