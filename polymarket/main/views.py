from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import RegisterForm
from .models import Service


def index(request):
    return render(request, 'main/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main')


class AccountLoginView(LoginView):
    template_name = 'main/login.html'


class CatalogView(ListView):
    model = Service
    template_name = 'main/catalog.html'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)
