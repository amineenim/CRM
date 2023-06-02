from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, NewRecordForm
from website.models import Record

# Create your views here.
# the home page view 
def home(request) : 
    # grab all recors 
    records = Record.objects.all()
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
    return render(request, 'home.html', {'records' : records})

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
         
# function that handles returning view for a single record 
def view_record(request, id) :
    if request.user.is_authenticated : 
        # grab the corresponding record 
        record = Record.objects.filter(id =id)
        if record : 
            return render(request, 'record.html', {'record' : record[0]})
        else :
            return render(request, '404.html')
    else : 
        messages.error(request, "Authentication required !")
        return redirect('home')

# function that handles deleting a record 
def delete_record(request, id) : 
    if request.user.is_authenticated :
        # get the instance to delete 
        record = Record.objects.get(id=id)
        record.delete()
        messages.success(request, "Record deleted successfully !")
        return redirect("home")
    else : 
        messages.error(request, "Authentication required !")
        return redirect('home')

# function that handles creating a new record 
def create_record(request) : 
    form = NewRecordForm(request.POST or None)
    if request.user.is_authenticated : 
        if request.method == "POST" :
            if form.is_valid() :
                form.save()
                messages.success(request, "Record Added Successfully !")
                return redirect('home')
        else :
            return render(request, 'new.html', {'form' : form})
    else :
        messages.error(request, "Authentication required !")
        return redirect('home')

# function that handles editing a given record resource 
def edit_record(request, id) : 
    if request.user.is_authenticated :
        # grab the record to update
        record_to_update = Record.objects.get(id=id) 
        if request.method == "POST" :
            # pass it to the form so it can be prefilled 
            form = NewRecordForm(request.POST, instance=record_to_update)
            if form.is_valid() :
                form.save()
                messages.success(request, "Record Updated Successfully")
                return redirect('home')
        # if the form has not been submitted 
        form = NewRecordForm(instance=record_to_update)
        return render(request, 'update_record.html', {'form' : form})
    else :
        messages.error(request, "Authentication required !")
        return redirect('home')


