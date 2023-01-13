from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/login/', views.CoreLoginView.as_view(), name='login'),
    path('auth/logout/', views.CoreLogoutView.as_view(), name='logout'),
    path('servidores/',views.ServidorList.as_view(), name='lista_servidores'),
    path('cadastrar-servidor/',views.ServidorView.as_view(), name='cadastrar_servidor'),
    path('alunos/', views.AlunoList.as_view(), name='lista_alunos'),
    path('cadastrar-aluno/',views.AlunoView.as_view(), name='cadastrar_aluno'),
    path('turmas/',views.TurmaList.as_view(), name='lista_turmas'),
    path('cadastrar-turma/',views.TurmaView.as_view(), name='cadastrar_turma'),
    path('atualizar/servidores/<int:pk>/', views.post_update, name='servidor_update'),
    path('deletar/servidores/<int:id>/', views.servidor_delete , name='servidor_delete'),
]
