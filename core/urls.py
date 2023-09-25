"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from controle.views.alunosListCreateView import AlunoListCreateView
from controle.views.alunoRetrieveUpdateDeleteView import AlunoRetrieveUpdateDeleteView
from controle.views.disciplinaListCreateView import DisciplinaListCreateView
from controle.views.disciplinaRetrieveUpdateDeleteView import DisciplinaRetrieveUpdateDeleteView
from controle.views.tarefaListCreateView import TarefaListCreateView
from controle.views.tarefaRetrieveUpdateDeleteView import TarefaRetrieveUpdateDeleteView
from controle.views.alunotarefaListView import AlunoTarefaListView


urlpatterns = [
    path('aluno/', AlunoListCreateView.as_view(), name='aluno-list-create'),
    path('api/aluno/<int:pk>/', AlunoRetrieveUpdateDeleteView.as_view(), name='aluno-detail'),
    path('disciplinas/', DisciplinaListCreateView.as_view(), name='disciplina-list-create'),
    path('api/disciplinas/<int:pk>/',DisciplinaRetrieveUpdateDeleteView.as_view(), name='disciplina-detail'),
    path('tarefas/', TarefaListCreateView.as_view(), name='tarefa-list-create'),
    path('api/tarefas/<int:pk>/', TarefaRetrieveUpdateDeleteView.as_view(), name='tarefa-detail'),
    path('api/alunos/<int:aluno_id>/tarefas/', AlunoTarefaListView.as_view(), name='aluno-tarefa-list'),
    ]



