from django.shortcuts import render, redirect
from django import forms

from .utils import *


class LoginForm(forms.Form):
    login = forms.CharField(label="Enter your login", max_length=10)
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput, max_length=15)


def index(request):
    if request.POST:
        data = request.__dict__['_post']
        data_processing(data['login'], data['password'])
    form = LoginForm()
    return render(request, 'login/login_page.html', {'form': form})


