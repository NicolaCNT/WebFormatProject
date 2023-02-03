from django import forms
from .models import *

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','deadline', 'status', 'created_by']

class AssignTaskToDevForm(forms.ModelForm):
    class Meta:
        model = TaskAssigned
        fields = ['developer', 'task']