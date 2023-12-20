from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import RegisterForm


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
