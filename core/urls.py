from django.urls import path
from core import views
from django.conf.urls.static import static
from ge import settings


app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/login/', views.CoreLoginView.as_view(), name='login'),
    path('auth/logout/', views.CoreLogoutView.as_view(), name='logout'),
    path('servidores/',views.ServidorList.as_view(), name='lista_servidores'),
    path('relatorios/',views.relatorio, name='ge_relatorios'),
    path('cadastrar-servidor/',views.ServidorView.as_view(), name='cadastrar_servidor'),
    path('visualizar/servidores/<int:pk>',views.ServidorVisualizar.as_view(), name='visualizar_servidor'),
    path('visualizar/alunos/<int:pk>',views.AlunoVisualizar.as_view(), name='visualizar_aluno'),
    path('alunos/', views.AlunoList.as_view(), name='lista_alunos'),
    path('cadastrar-aluno/',views.AlunoView.as_view(), name='cadastrar_aluno'),
    path('turmas/',views.TurmaList.as_view(), name='lista_turmas'),
    path('cadastrar-turma/',views.TurmaView.as_view(), name='cadastrar_turma'),
    path('atualizar/servidores/<int:pk>/', views.post_update, name='servidor_update'),
    path('atualizar/alunos/<int:pk>/', views.post_update_aluno, name='aluno_update'),
    path('deletar/servidores/<int:id>/', views.servidor_delete , name='servidor_delete'),
    path('deletar/alunos/<int:id>/', views.aluno_delete , name='aluno_delete'),
    path('servidores/servidores.pdf/', views.servidores_pdf , name='servidores_pdf'),
    path('alunos/pdf/', views.alunos_pdf , name='alunos_pdf'),
    path('matriculas/pdf/', views.matriculas_pdf , name='matriculas_pdf'),
    path('turmas/pdf/', views.turmas_pdf , name='turmas_pdf'),
    path('visualizar/turmas/<int:pk>/',views.TurmaVisualizar.as_view(), name='visualizar_turma'),
    path('editar/turmas/<int:pk>/',views.post_update_turma, name='editar_turma'),
    path('deletar/turmas/<int:id>/', views.turma_delete , name='turma_delete'),
    path('escola/', views.EscolaView.as_view() , name='visualizar_escola'),
    path('professor/', views.ProfessorView.as_view() , name='home_professor'),
    path('lotacoes/delete/<int:pk>/', views.lotacao_delete, name='lotacao_delete'),
    path('turmas/<int:pk>/lotacoes/', views.LotacaoList.as_view(), name='lista_lotacoes'),
    path('turmas/<int:pk>/lotacoes/add/', views.LotacaoView.as_view(), name='cadastrar_lotacao'),
    path('lotacoes/<int:pk>/edit/', views.LotacaoEdit.as_view(), name='editar_lotacao'),
    path('matriculas/add/', views.MatriculaCreateView.as_view(), name='cadastrar_matricula'),
    path('matriculas/', views.MatriculaListView.as_view(), name='listar_matricula'),
    path('matriculas/delete/<int:pk>/', views.matricula_delete, name='matricula_delete'),
    path('matriculas/<int:pk>/', views.MatriculaVisualizar.as_view(), name='visualizar_matricula'),
    path('matriculas/<int:pk>/edit/', views.MatriculaEdit.as_view(), name='editar_matricula'),
]