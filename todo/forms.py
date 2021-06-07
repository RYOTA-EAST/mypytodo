from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):

  class Meta:
    model = Todo
    fields = ('title', 'body', 'status','deadline')
    widgets = {
      'deadline' : forms.SelectDateWidget 
    }