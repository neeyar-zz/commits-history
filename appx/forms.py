from django import forms

class NameForm(forms.Form):
	add = forms.CharField(label="Full name", max_length=100)