from django import forms
from .models import *

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','deadline', 'created_by']

