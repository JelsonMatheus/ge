from django.views.generic import TemplateView,FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsuarioForms, AlunoForms


class BaseView(LoginRequiredMixin):
    """
    Classe base para as demais views que requer um usuário logado.
    """
    login_url = '/auth/login/'


class CoreLoginView(LoginView):
    """
    View para login do Diretor ou Professor.
    """
    template_name = 'core/registration/login.html'
    redirect_authenticated_user = True
    next_page = 'core:index'


class CoreLogoutView(LogoutView):
    """
    View para deslogar o Diretor ou Professor.
    """
    next_page = 'core:index'


class IndexView(BaseView, TemplateView):
    template_name = 'core/index.html'

class ServidorView(BaseView, FormView):
    form_class = UsuarioForms
    template_name = 'core\cadastrar_servidor.html'

class AlunoView(BaseView, FormView):
    form_class = AlunoForms
    template_name = 'core\cadastrar_aluno.html'
