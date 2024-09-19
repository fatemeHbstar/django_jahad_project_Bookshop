from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'sample@gmail.com'}))
    password_1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
    password_2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'repeat password'}))

    def clean_username(self):
        user = self.cleaned_data['username']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError("Username exists")
        else:
            return user

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email exists")
        else:
            return email

    def clean_password_2(self):
        pass1 = self.cleaned_data['password_1']
        pass2 = self.cleaned_data['password_2']
        if pass1 != pass2:
            raise forms.ValidationError("Passwords don't match")
        elif len(pass1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters")
        elif pass2.isdigit() or pass2.isalpha():
            raise forms.ValidationError("Password must have at least one character and one number")
        elif not any(c.isupper() for c in pass1):
            raise forms.ValidationError("Password must have at least one uppercase character")
        else:
            return pass1


class UserLoginForm(forms.Form):
    user = forms.CharField(max_length=30)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'password'}))


class PurchaseForm(forms.Form):
    old_pass = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'enter old password'}))
    new_pass1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'enter new password'}))
    new_pass2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'enter new password'}))
