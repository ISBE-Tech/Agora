from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Enter name', max_length=25)
    email = forms.CharField(label='Your email', max_length=30)
    score = forms.IntegerField(label='Your score')