from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, \
    DetailView, RedirectView
from .forms import RegisterForm
from .models import *


def index(request):
    return render(request, 'main/index.html')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')


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
    fields = ['title', 'price', 'description', 'picture', 'is_active']
    template_name = 'main/create_service.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class UpdateServiceView(UpdateView):
    model = Service
    fields = ['title', 'price', 'description', 'picture', 'is_active']
    template_name = 'main/update_service.html'
    success_url = reverse_lazy('catalog')

    def form_valid(self, form):
        if form.instance.owner.id == self.request.user.id:
            return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class ServiceView(DetailView):
    model = Service
    template_name = 'main/service.html'


class ProfileView(DetailView):
    model = Account
    template_name = 'main/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.filter(owner__id=self.kwargs.get(
            'pk'))
        return context


class UpdateAccountView(UpdateView):
    model = Account
    fields = ['about', 'avatar']
    template_name = 'main/update_account.html'

    def get_success_url(self):
        success_url = reverse_lazy('profile', kwargs={'pk': self.object.pk})
        return success_url

    def form_valid(self, form):
        if form.instance.id == self.request.user.id:
            return super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class OrderView(RedirectView):
    url = '/catalog/'

    def get_redirect_url(self, *args, **kwargs):
        buyer = self.request.user
        service = get_object_or_404(Service, pk=kwargs['pk'])
        if buyer.id == service.owner.id:
            return super().get_redirect_url(*args, **kwargs)
        new_order = Order.objects.create(buyer=buyer, service=service)
        new_order.update_counter()
        return super().get_redirect_url(*args, **kwargs)
