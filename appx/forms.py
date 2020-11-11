from django import forms

class NameForm(forms.Form):
	add = forms.CharField(label="Repo name", max_length=100)