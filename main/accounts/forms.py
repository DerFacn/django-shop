from django import forms

class RegForm(forms.Form):
    login = forms.CharField(label='Login', max_length=100)