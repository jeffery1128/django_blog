from attr import attr
from django import forms
from blog.models import post,comment

class PostForm(forms.ModelForm):

    class Meta():
        model = post
        fields = ('author','title','text')

        widgets={
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = comment
        fields = ('author','text')

        widgets={
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }