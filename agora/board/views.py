from django.shortcuts import render
from django.http import HttpResponse
from forms import UserForm
from models import *

# Create your views here.
def display_page(request):
	posts = Post.objects.all()
	users = User.objects.all()
	context = {'myform':UserForm, 'posts':posts, 'users':users}
	return render(request, 'page.html', context)

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UserForm(request.POST)
        name_from_form = request.POST['name']
        email_from_form = request.POST['email']
        score_from_form = request.POST['score']
        user = User(name=name_from_form, email=email_from_form)
        user.score = score_from_form
        user.save()
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse('<marquee>Thanks!!!!!!!!!</marquee>')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UserForm()

    return render(request, 'page.html', {'form': form})


