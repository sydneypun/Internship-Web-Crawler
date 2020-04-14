from django.forms import ModelForm
from django import forms
from web_application.app_core.models import Resume
from django.forms import ClearableFileInput


class ResumeModelForm(forms.ModelForm):

	class Meta:
		model = Resume
		fields = [
			'pdf',
			'industry'
		]
		widgets = {
		'pdf': ClearableFileInput(attrs = {'multiple': True}),
		}