from django import forms
from django.core import validators

class FormName(forms.Form):
    name = forms.CharField()
    Email = forms.EmailField()

    verify_email = forms.EmailField(label='Enter your email again: ')

    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data = super().clean()
        Email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        if Email != vmail:
            raise forms.ValidationError('does not match')
