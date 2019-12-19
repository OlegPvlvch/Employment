from django.shortcuts import render
from django.contrib.auth import views

class MyLoginView(views.LoginView):
    template_name = 'login_app/login.html'
