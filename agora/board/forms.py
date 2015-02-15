from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Enter name', max_length=25)
    email = forms.CharField(label='Your email', max_length=30)
    score = forms.IntegerField(label='Your score')

class PostForm(forms.Form):
	title = forms.CharField(label='Post title', max_length=100)
	text = forms.CharField(label='Post content', max_length=1500)
	tag = forms.CharField(label='Tag', max_length=20)