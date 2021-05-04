from django import forms
from blog.models import Post,Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')
        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}), #these classes are not yet defined
            'text':forms.TextInput(attrs={'class': 'editable medium-editor-textarea postcontent'}) #we can stack classes on each other by sep them by space
        }
    
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author','text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}) ,
            'text': forms.TextInput(attrs={'class': 'editable medium-editor-textarea'})

        }
