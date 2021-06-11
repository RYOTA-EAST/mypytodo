from django import forms
from .models import Todo
import bootstrap_datepicker_plus as datetimepicker

class TodoForm(forms.ModelForm):

  class Meta:
    model = Todo
    fields = ('title', 'body', 'status','deadline')
    widgets = {
          'deadline': datetimepicker.DateTimePickerInput(
                format='%Y-%m-%d %H:%M',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                })
    }