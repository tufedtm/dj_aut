from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, RedirectView, CreateView

from .forms import UserRegistrationForm


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'prj_auth/home.html'
    login_url = reverse_lazy('prj_auth:login')


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'prj_auth/login.html'
    success_url = reverse_lazy('prj_auth:home')

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('prj_auth:login')

    def get(self, request, *args, **kwargs):
        logout(request)

        return super(LogoutView, self).get(request, *args, **kwargs)


class RegistrationView(CreateView):
    template_name = 'prj_auth/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('prj_auth:home')

    def form_valid(self, form):
        valid = super(RegistrationView, self).form_valid(form)

        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)

        return valid
