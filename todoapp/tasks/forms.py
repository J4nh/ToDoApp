from django import forms
from django.forms import ModelForm
from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    end_date = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Due date...'}), label=False)


    class Meta:
        model = Task
        fields = ['title', 'end_date']

class UpdateForm(forms.ModelForm):
	title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task title...'}))

	class Meta:
		model = Task
		fields = ['title', 'end_date', 'complete']