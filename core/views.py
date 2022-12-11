from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class BaseView(LoginRequiredMixin):
    login_url = '/auth/login/'


class IndexView(BaseView, TemplateView):
    template_name = 'core/index.html'


class CoreLoginView(LoginView):
    template_name = 'core/registration/login.html'
    redirect_authenticated_user = True
    next_page = 'core:index'