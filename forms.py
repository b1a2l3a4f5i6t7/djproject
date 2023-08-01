from django import forms
from fapp.models import student
class StudentModelForm(forms.ModelForm):
	class Meta:
		model=student
		fields='__all__'
