from django.contrib.messages.api import warning
from django.shortcuts import render, redirect
from django.contrib import messages

from users.models import Profile
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

# this is a django class that creates HTML based on Python code
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', context)




# """ documentation

# first some django imports that allow redirects and the render (essentially a shortcut for something I am hazy on)
# from forms.py imports a class of UserRegisterForm which adds an email

# then defines the function register which requires a request

# the POST is a dictionary-like object that lets you access submitted data by key name
#     then checks if form is valid (a python method), and saves the record. sets a variable 'username' and returns a success message template, finally redirecting user to home page

# the else statement reloads the form with some saved info and then the crispy form gives errors to user

# """



