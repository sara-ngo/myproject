from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) # using self-create form instead of lib form because it doesn't have email field
        if form.is_valid():
            user = form.save() # create a user instance
            auth_login(request, user) # manually authenticating the user
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request,'signup.html', {'form':form})