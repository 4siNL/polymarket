from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView
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


class AccountLogoutView(LogoutView):
    pass


class CatalogView(ListView):
    model = Service
    template_name = 'main/catalog.html'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)


class DeleteServiceView(DeleteView):
    model = Service
    success_url = reverse_lazy('catalog')
    template_name = 'main/delete_service.html'

    def form_valid(self, form):
        if self.object.owner.id == self.request.user.id:
            return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class CreateServiceView(CreateView):
    model = Service
    fields = ['title', 'price', 'description', 'picture']
    template_name = 'main/create_service.html'
    success_url = reverse_lazy('catalog')
