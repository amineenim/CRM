from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    pass 