from django.views.generic import TemplateView, ListView , DetailView 
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsuarioForms, AlunoForms, TurmaForms, UsuarioFormsEdit, AlunoFormsEdit
from core.models import Usuario, Aluno, Turma
from django.shortcuts import redirect,render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse

from core import report
from reportlab.platypus import Paragraph



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

class EscolaView(BaseView, TemplateView):
    template_name = 'core/escola.html'

class ServidorList(BaseView, ListView):
    model = Usuario
    template_name = 'core/servidores.html'
    paginate_by =4

    def get_queryset(self):
        nome_input = self.request.GET.get('nome')
        if nome_input:
            servidor = Usuario.objects.filter(nome__icontains=nome_input)
        else:
            servidor = Usuario.objects.all()
        return servidor

class ServidorVisualizar(BaseView, DetailView):
    model = Usuario
    template_name = 'core/visualizar_servidor.html'



class AlunoList(BaseView, ListView):
    model = Aluno
    template_name = 'core/alunos.html'
    paginate_by = 4

    def get_queryset(self):
        nome_input = self.request.GET.get('nome')
        if nome_input:
            aluno = Aluno.objects.filter(nome__icontains=nome_input)
        else:
            aluno = Aluno.objects.all()
        return aluno

class AlunoVisualizar(BaseView, DetailView):
    model = Aluno
    template_name = 'core/visualizar_aluno.html'


class TurmaList(BaseView, ListView):
    model = Turma
    template_name = 'core/turmas.html'
    paginate_by = 4

    def get_queryset(self):
        nome_input = self.request.GET.get('nome')
        if nome_input:
            turma = Turma.objects.filter(nome__icontains=nome_input)
        else:
            turma = Turma.objects.all()
        return turma


class ServidorView(BaseView, CreateView):
    form_class = UsuarioForms
    template_name = 'core/cadastrar_servidor.html'
    success_url = '/servidores/'
class ProfessorView(BaseView,TemplateView):
    template_name = 'core/homeProfessor.html'

class AlunoView(BaseView, CreateView):
    form_class = AlunoForms
    template_name = 'core/cadastrar_aluno.html'
    success_url = '/alunos/'
    


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


class TurmaVisualizar(BaseView, DetailView):
    model = Turma
    template_name = 'core/visualizar_turma.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dia_selecionado = []
        dias = self.object.dia_semana.split(",")
        dia = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 
                'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo']
        for d in dias:
            dia_selecionado.append(dia[int(d)])

        context['dia_selecionado'] = dia_selecionado
        return context


def relatorio(request):
    context = {}
    masculino = Usuario.objects.filter(sexo='M').count()
    feminino = Usuario.objects.filter(sexo='F').count()

    matutino = Turma.objects.filter(turno='M').count()
    vespertino = Turma.objects.filter(turno='V').count()
    noturno = Turma.objects.filter(turno='N').count()

    urbana = Aluno.objects.filter(zona='U').count()
    rural = Aluno.objects.filter(zona='R').count()

    ens_fundamental = Turma.objects.filter(tipo_atendimento='1').count()
    ens_medio = Turma.objects.filter(tipo_atendimento='2').count()

    context[ 'masculino'] = masculino
    context[ 'feminino'] = feminino
    context[ 'matutino'] = matutino
    context[ 'vespertino'] = vespertino
    context[ 'noturno'] = noturno
    context[ 'urbana'] = urbana
    context[ 'rural'] = rural
    context[ 'ens_fundamental'] = ens_fundamental
    context[ 'ens_medio'] = ens_medio
    return render(request, 'core/relatorio.html', context=context)

def servidor_delete(request,id):
    servidor = get_object_or_404(Usuario, pk=id)
    servidor.delete()
    return redirect('/servidores/')

def aluno_delete(request,id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno.delete()
    return redirect('/alunos/')

def turma_delete(request,id):
    turma = get_object_or_404(Turma, pk=id)
    turma.delete()
    return redirect('/turmas/')

    
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

def post_update_turma(request, pk):
    turma = get_object_or_404(Turma, pk=pk)
    form = TurmaForms(instance=turma)

    if(request.method == 'POST'):
        form = TurmaForms(request.POST, instance=turma)
        
        if(form.is_valid()):
            form.save(commit=True)
            return redirect(reverse("core:lista_turmas"))
        else:
            return render(request, 'core/cadastrar_turma.html', {'form': form, 'turma' : turma})
    elif(request.method == 'GET'):
        return render(request, 'core/cadastrar_turma.html', {'form': form, 'turma' : turma})

###################### Gerando pdf ##########
def servidores_pdf(request):
    servidores = [['Nome', 'Nascimento', 'CPF', 'Sexo', 'Email', 'Endereço']]
    
    for servidor in Usuario.objects.all():
        Paragraph('YITUTOPABDASJHVDAUYDVHJ')
        servidores.append([
            Paragraph(servidor.nome),
            Paragraph(str(servidor.data_nascimento)),
            Paragraph(servidor.cpf),
            Paragraph(servidor.get_sexo_display()),
            Paragraph(servidor.email),
            Paragraph(servidor.endereco)
        ])
    return report.report_servidor(servidores)

def alunos_pdf(request):
    alunos = [['Nome', 'Nascimento', 'CPF', 'Sexo', 'Mãe', 'Pai', 'Responsável']]
    for aluno in Aluno.objects.all():
        alunos.append([
            Paragraph(aluno.nome),
            Paragraph(str(aluno.data_nascimento)),
            Paragraph(aluno.cpf),
            Paragraph(aluno.get_sexo_display()),
            Paragraph(aluno.nome_da_mae),
            Paragraph(aluno.nome_do_pai),
            Paragraph(aluno.get_responsavel_display())
        ])
    return report.report_aluno(alunos)
	

def turmas_pdf(request):
    turmas = [['Nome', 'Turno', 'Modalidade', 'Sala']]
    for turma in Turma.objects.all():
        turmas.append([
            Paragraph(turma.nome),
            Paragraph(turma.get_turno_display()),
            Paragraph(turma.get_tipo_atendimento_display()),
            Paragraph(str(turma.sala))
        ])
    return report.report_turma(turmas)


