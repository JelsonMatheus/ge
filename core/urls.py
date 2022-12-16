from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('auth/login/', views.CoreLoginView.as_view(), name='login'),
    path('auth/logout/', views.CoreLogoutView.as_view(), name='logout'),
    path('cadastrar_servidor/',views.ServidorView.as_view(),name='cadastrar_servidor'),
    path('cadastrar_aluno/',views.AlunoView.as_view(),name='cadastrar_aluno'),
    path('cadastrar_turma/',views.TurmaView.as_view(),name='cadastrar_turma'),
]
