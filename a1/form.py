from django import forms

class VocabForm(forms.Form):
    guess = forms.CharField(max_length=20, required=True)