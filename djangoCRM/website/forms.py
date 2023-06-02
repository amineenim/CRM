from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm) :
    email = forms.EmailField(label="Email Adress :", widget= forms.TextInput(attrs={
        'class' : "border rounded-xl pl-5 py-2 w-full flex flex-col mb-3 mt-2",
        'placeholder' : "your Email Adress" 
    }))
    first_name = forms.CharField(label="First name :", max_length= 60, widget= forms.TextInput(attrs= {
        'class' : "border rounded-xl pl-5 py-2 w-full flex flex-col mb-3 mt-2",
        'placeholder' : "Type In your First Name"
    }))
    last_name = forms.CharField(label= "Last Name :", max_length= 60, widget= forms.TextInput(attrs={
        'class' : "border rounded-xl pl-5 py-2 w-full flex flex-col mb-3 mt-2",
        'placeholder' : "Type In your Last Name"
    }))

    class Meta : 
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = "User Name :"
        self.fields['username'].widget.attrs['class'] = "border rounded-xl pl-5 py-2 mt-2 w-full flex flex-col"
        self.fields['username'].widget.attrs['placeholder'] = "Type In your User Name"
        self.fields['username'].help_text = '<span class="text-sm py-3 ml-3 mb-2">Required, 60 characters or fewer, Letters, digits and @/ ./+/-/_ only</span>'

        self.fields['password1'].label = "Password :"
        self.fields['password1'].widget.attrs['class'] = "border rounded-xl pl-5 py-2 mt-2 w-full flex flex-col"
        self.fields['password1'].widget.attrs['placeholder'] = "Type In Your Paasword"
        self.fields['password1'].help_text = '<ul class="list-disc my-4 ml-8"><li class="text-sm">Your password can\'t be similar to your other personal informatiom</li><li class="text-sm">Your Password must at least contain 8 characters.</li><li class="text-sm">Your password can\'t be a commonly used password.</li><li class="text-sm">Your Password can\'t be entirely numeric.</li></ul> '


        self.fields['password2'].label = "Password Confirmation:"
        self.fields['password2'].widget.attrs['class'] = "border rounded-xl pl-5 py-2 mt-2 w-full flex flex-col"
        self.fields['password2'].widget.attrs['placeholder'] = "Confirm your Password"
        self.fields['password2'].help_text = '<span class="text-sm py-3 ml-3">Enter the same password for verification</span>'