from django import forms
from component.models import Application


class ApplicationForm(forms.ModelForm):
	name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}))
	technology = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Technology'}))
	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description'}))
	 
	class Meta:
		model = Application
		fields = ['name', 'technology', 'description']