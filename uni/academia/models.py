from django.db import models

# Create your models here.
class Carrera(models.Model):
    codigo = models.PositiveSmallIntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.IntegerField()

    def __str__(self):
        return f'Codigo: {self.codigo} | Nombre: {self.nombre} | Duracion: {self.duracion}'


class Estudiante(models.Model):
    dni = models.PositiveBigIntegerField(primary_key=True)
    apellido_paterno = models.CharField(max_length=35, blank=True)
    apellido_materno = models.CharField(max_length=35, blank=True)
    nombres = models.CharField(max_length=35)
    fecha_nacimiento = models.DateField()
    sexos = [('F','Femenino'),('M','Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos)
    codigo_carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE,blank=False, null=False)
    vigencia = models.BooleanField()

    def nombre_completo(self):
        txt = '{0} {1} {2}'
        return txt.format(self.apellido_paterno, self.apellido_materno, self.nombres)


    def __str__(self):
        txt = '{0} / Carrera: {1} / {2}'
        if self.vigencia:
            estadoEstudiante = 'Vigente'
        else:
            estadoEstudiante = 'De Baja'
        return txt.format(self.nombre_completo(), self.codigo_carrera, estadoEstudiante)


class Docente(models.Model):
    dni = models.PositiveBigIntegerField(primary_key=True)
    apellido_paterno = models.CharField(max_length=35, blank=True)
    apellido_materno = models.CharField(max_length=35, blank=True)
    nombres = models.CharField(max_length=35)
    fecha_nacimiento = models.DateField()
    sexos = [('F', 'FEemenino'), ('M', 'Masculino')]
    sexo = models.CharField(max_length=1, choices=sexos)
    titulo = models.CharField(max_length=50)


    def __str__(self):
        return f'DNI: {self.dni} | Nombre completo: {self.apellido_paterno} {self.apellido_materno} {self.nombres}' \
               f'Fecha de Nacimiento: {self.fecha_nacimiento} | Sexo: {self.sexo} | Titulo: {self.titulo}'



class Curso(models.Model):
    codigo = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.IntegerField()
    docente = models.ForeignKey(Docente,on_delete=models.CASCADE,blank=False, null=False)

    def __str__(self):
        return f'Codigo: {self.codigo} | Nombre: {self.nombre} | Creditos: {self.creditos} | Docente: {self.docente}'
