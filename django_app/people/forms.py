from django import forms

class AddPersonForm(forms.Form):
    name = forms.CharField(label="Name", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="Email", max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))