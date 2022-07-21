"""uni URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from academia.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',welcome,name='index'),

    #estructura para carrera
    path('carrera_home',career_home),

    #estructura para cursos
    path('curso_home',course_home),

    #estructura para estudiante
    path('estudiante_home',student_home,name='studentindex'),
    path('añadirestudiante',add_student),
    path('detalleestudiante/<int:id>',student_detail),
    path('editarestudiante/<int:id>',student_edit),
    path('eliminarestudiante/<int:id>',delete_student),




    #estructura para docentes
    path('docente_home',teach_home,name='teacher_home'),
    path('añadirdocente',add_teacher),
    path('editardocente/<int:id>',edit_teacher),
    path('detalledocente/<int:id>',detail_teacher),

]
