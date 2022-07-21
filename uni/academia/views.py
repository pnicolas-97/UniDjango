from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from academia.models import Carrera, Estudiante
from academia.forms import *


def welcome(request):
    return render(request, 'academy_home.html')

# Views Para estudiantes
def student_home(request):
    estudiante = Estudiante.objects.order_by('apellido_paterno')
    busqueda = request.GET.get('get_student')
    if busqueda:
        estudiante = Estudiante.objects.filter(
            Q(dni__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(apellido_paterno__icontains=busqueda) |
            Q(apellido_materno__icontains=busqueda)
        ).distinct()
    return render(request,'stdnt/estudiantes.html',{'estudiante':estudiante})

def add_student(request):
    if request.method == 'POST':
        formEstudent = EstudentForm(request.POST)
        if formEstudent.is_valid():
            formEstudent.save()
            return redirect('studentindex')
        else:
            return render(request,'stdnt/añadir_estudiante.html',{'formEstudent':formEstudent})
    else:
        formEstudent = EstudentForm()
        return render(request, 'stdnt/añadir_estudiante.html', {'formEstudent': formEstudent})


def student_detail(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    return render(request,'stdnt/detalle_estudiante.html',{'detalle':estudiante})


def student_edit(request, id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if request.method == 'POST':
        formEstudiante = EstudentForm(request.POST, instance=estudiante)
        if formEstudiante.is_valid():
            formEstudiante.save()
            return redirect('studentindex')
        else:
            return render(request,'stdnt/editar_estudiante.html',{'formEstudiante':formEstudiante})
    else:
        formEstudiante = EstudentForm(instance=estudiante)
        return render(request,'stdnt/editar_estudiante.html',{'formEstudiante':formEstudiante})


def delete_student(request,id):
    estudiante = get_object_or_404(Estudiante, pk=id)
    if estudiante:
        estudiante.delete()
        return redirect('studentindex')


#Views para docentes
def teach_home(request):
    docente = Docente.objects.order_by('dni')
    busqueda = request.GET.get('get_teacher')
    if busqueda:
        docente = Docente.objects.filter(
            Q(dni__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(apellido_paterno__icontains=busqueda) |
            Q(apellido_materno__icontains=busqueda)
        ).distinct()
    return render(request, 'tch/docentes.html',{'docente':docente})

def add_teacher(request):
    if request.method == 'POST':
        formDocente = DocenteForm(request.POST)
        if formDocente.is_valid():
            formDocente.save()
            return redirect('teacher_home')
        else:
            return render(request,'tch/añadir_docente.html',{'formDocente':formDocente})
    else:
        formDocente = DocenteForm()
        return render(request, 'tch/añadir_docente.html', {'formDocente': formDocente})

def edit_teacher(request, id):
    docente = get_object_or_404(Docente,pk=id)
    if request.method == 'POST':
        formDocente = DocenteForm(request.POST,instance=docente)
        if formDocente.is_valid():
            formDocente.save()
            return redirect('teacher_home')
        else:
            return render(request,'tch/editar_docente.html',{'formDocente':formDocente})
    else:
        formDocente = DocenteForm(instance=docente)
        return render(request, 'tch/editar_docente.html', {'formDocente': formDocente})

def detail_teacher(request,id):
    docente = get_object_or_404(Docente, pk=id)
    return render(request,'tch/detalle_docente.html',{'detalle':docente})

def delete_teacher(request, id):
    docente = get_object_or_404(Docente, pk=id)
    if docente:
        docente.save()
        return  redirect('teacher_home')






#Views para carreras
def career_home(request):
    carrera = Carrera.objects.order_by('codigo')
    return render(request, 'crr/carreras.html',{'carrera':carrera})


#Views para cursos
def course_home(request):
    cursos = Curso.objects.order_by('codigo')
    return render(request, 'crs/cursos.html',{'cursos':cursos})

