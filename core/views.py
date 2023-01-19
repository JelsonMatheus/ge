from django.views.generic import TemplateView, ListView , DetailView 
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UsuarioForms, AlunoForms, TurmaForms, UsuarioFormsEdit, AlunoFormsEdit
from core.models import Usuario, Aluno, Turma
from django.shortcuts import redirect,render, get_object_or_404

# Import PDF Stuff
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter



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


class ServidorView(BaseView, CreateView):
    form_class = UsuarioForms
    template_name = 'core/cadastrar_servidor.html'
    success_url = '/servidores/'
    


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


###################### Gerando pdf ##########
def servidores_pdf(request):
	
	buf = io.BytesIO()
	
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	
	
	servidores = Usuario.objects.all()

	
	lines = []

	for servidor in servidores:
        
		lines.append(servidor.cpf)
		lines.append(servidor.nome)
		lines.append(servidor.sexo)
		lines.append(servidor.telefone)
		lines.append(servidor.email)
		lines.append(servidor.estado_civil)
		lines.append(servidor.cep)
		lines.append(servidor.endereco)
		lines.append(servidor.zona)

		lines.append(" -------------------------------------------")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='servidores.pdf')


def alunos_pdf(request):
	
	buf = io.BytesIO()
	
	c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
	# Create a text object
	textob = c.beginText()
	textob.setTextOrigin(inch, inch)
	textob.setFont("Helvetica", 14)

	
	
	alunos = Aluno.objects.all()

	
	lines = []

	for aluno in alunos:
        
		lines.append(aluno.cpf)
		lines.append(aluno.nome)
		lines.append(aluno.sexo)
		lines.append(aluno.nome_da_mae)
		lines.append(aluno.nome_do_pai)
		lines.append(aluno.responsavel)
		lines.append(aluno.email)
		lines.append(aluno.estado_civil)
		lines.append(aluno.cep)
		lines.append(aluno.endereco)
		lines.append(aluno.zona)

		lines.append(" -------------------------------------------")

	# Loop
	for line in lines:
		textob.textLine(line)

	# Finish Up
	c.drawText(textob)
	c.showPage()
	c.save()
	buf.seek(0)

	# Return something
	return FileResponse(buf, as_attachment=True, filename='alunos.pdf')