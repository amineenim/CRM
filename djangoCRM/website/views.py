from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

# Create your views here.
# the home page view 
def home(request) : 
    # check if the form is submitted
    if request.method == "POST" :
        # get form data
        username = request.POST['username']
        password = request.POST['password']
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None :
            login(request, user)
            messages.success(request,"Welcome back !")
            return redirect('home')
        else :
            messages.error(request, "something went wrong, please verify your credentials !")
            return redirect('home')
    return render(request, 'home.html', {})

# function that handles login in a user
def login_user(request) :
    pass

# function that handles logging out a user
def logout_user(request) : 
    logout(request)
    messages.success(request, "Logged out with success !")
    return redirect('home')

# function that handles registering a user 
def register_user(request) :
    # if the registration form is submitted
    if request.method == 'POST' :
        form = SignUpForm(request.POST)
        if form.is_valid() :
            form.save()
            # authenticate the user and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request,user)
            messages.success(request, "You have successfully registred !")
            return redirect('home')
    else :
        form = SignUpForm()
        return render(request, 'register.html', {'form' : form})
    
    return render(request, 'register.html', {'form' : form})
         
