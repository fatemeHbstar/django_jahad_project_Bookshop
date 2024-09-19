from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404, reverse

from books.models import Book
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.models import User


# Create your views here.
def signin(request):
    if request.method == 'POST':
        form_register = UserRegisterForm(request.POST)
        if form_register.is_valid():
            data = form_register.cleaned_data
            User.objects.create_user(username=data['username'],
                                     email=data['email'],
                                     password=data['password_2'])
            return redirect('customer:login')
    else:
        form_register = UserRegisterForm()
    context = {'form_register': form_register}
    return render(request, 'customer/customer.html', context=context)


def viewlogin(request):
    if request.method == 'POST':
        form_login = UserLoginForm(request.POST)
        if form_login.is_valid():
            data = form_login.cleaned_data
            try:
                user = authenticate(request, username=User.objects.get(email=data['user']),
                                    password=data['password'])
            except:
                user = authenticate(request, username=data['user'],
                                    password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('customer:customer_page')
            else:
                return HttpResponse('Invalid login or password.')

    else:
        form_login = UserLoginForm()
    context = {'form_login': form_login}
    return render(request, 'customer/login.html', context=context)


def viewlogout(request):
    logout(request)
    return redirect('home:homepage')


@login_required()
def customer(request):
    user = request.user
    return render(request, 'customer/customer_page.html', {'user': user})
