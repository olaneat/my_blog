from django import  forms
from .models import Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')

class EmailPost(forms.Form):
  name = forms.CharField(max_length = 50)
  email = forms.EmailField()
  to = forms.EmailField()
  Comments = forms.CharField(required = False, widget = forms.Textarea)

