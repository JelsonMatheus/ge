from django.views.generic import TemplateView, ListView , DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsuarioForms, AlunoForms, TurmaForms, UsuarioFormsEdit, AlunoFormsEdit
from core.models import Usuario, Aluno, Turma
from django.shortcuts import redirect,render, get_object_or_404

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


class ServidorList(BaseView, ListView):
    model = Usuario
    template_name = 'core/servidores.html'

class ServidorVisualizar(BaseView, DetailView):
    model = Usuario
    template_name = 'core/visualizar_servidor.html'



class AlunoList(BaseView, ListView):
    model = Aluno
    template_name = 'core/alunos.html'
    paginate_by = 4


class TurmaList(BaseView, ListView):
    model = Turma
    template_name = 'core/turmas.html'


class ServidorView(BaseView, CreateView):
    form_class = UsuarioForms
    template_name = 'core/cadastrar_servidor.html'
    success_url = '/servidores/'



class AlunoView(BaseView, CreateView):
    form_class = AlunoForms
    template_name = 'core/cadastrar_aluno.html'
    success_url = '/alunos/'
    
    def get_queryset(self):

        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            aluno = Aluno.objects.filter(nome__icontains=txt_nome)
        else:
            Aluno = Aluno.objects.all()

        return aluno



class TurmaView(BaseView, CreateView):
    form_class = TurmaForms
    template_name = 'core/cadastrar_turma.html'
    success_url = '/turmas/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dias = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 
                'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        context['dias'] = dias
        return context


def servidor_delete(request,id):
    servidor = Usuario.objects.get(id=id)
    servidor.delete()
    return redirect('/servidores/')

def aluno_delete(request,id):
    aluno = Aluno.objects.get(id=id)
    aluno.delete()
    return redirect('/alunos/')
    
def visualizar_servidor(request, id, ListView):
    servidor = get_object_or_404(Usuario, id=id)
    model = UsuarioForms
    TemplateView = ServidorView
    return render(request, 'core/visualizar_servidor.html', {'servidor' : servidor})
    

#################UPDATE#################

def post_update(request, pk):
    servidor = get_object_or_404(Usuario, pk=pk)
    form = UsuarioFormsEdit(instance=servidor)
    if(request.method == 'POST'):
        form = UsuarioFormsEdit(request.POST, instance=servidor)
        
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/servidores/')
        else:
            return render(request, 'core/editar_servidor.html', {'form': form, 'servidor' : servidor})
    elif(request.method == 'GET'):
        return render(request, 'core/editar_servidor.html', {'form': form, 'servidor' : servidor})

def post_update_aluno(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoFormsEdit(instance=aluno)
    if(request.method == 'POST'):
        form = AlunoFormsEdit(request.POST, instance=aluno)
        
        if(form.is_valid()):
            form.save(commit=True)
            return redirect('/alunos/')
        else:
            return render(request, 'core/editar_aluno.html', {'form': form, 'aluno' : aluno})
    elif(request.method == 'GET'):
        return render(request, 'core/editar_aluno.html', {'form': form, 'aluno' : aluno})