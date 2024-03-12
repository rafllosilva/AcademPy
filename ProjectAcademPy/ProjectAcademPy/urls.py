"""
URL configuration for ProjectAcademPy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from AcademPy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view),
    path('cadastro-adm/', views.cadastro_adm_view),
    path('cadastro-professor/', views.cadastro_professor_view),
    path('criar-cronograma/', views.criar_cronograma_view),
    path('cronograma/', views.cronograma_view),
    path('disciplinas/', views.disciplinas_view),
    path('editar-disciplina/<int:id>', views.editar_disciplina_view, name='editar-disciplina'),
    path('editar-turma/<int:id>', views.editar_turma_view, name='editar-turma'),
    path('entrar/', views.entrar_view),
    path('excluir-disciplina/<int:id>', views.excluir_disciplina_view, name='excluir-disciplina'),
    path('excluir-turma/<int:id>', views.excluir_turma_view, name='excluir-turma'),
    path('home/', views.home_view),
    path('logout/', views.logout_view),
    path('minha-conta/', views.minha_conta_view),
    path('professores/', views.professores_view),
    path('redes-sociais/', views.redes_sociais_view),
    path('turmas/', views.turmas_view),
]
