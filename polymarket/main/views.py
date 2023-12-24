from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm


def index(request):
    return render(request, 'main/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main')


class AccountLoginView(LoginView):
    template_name = 'main/login.html'
