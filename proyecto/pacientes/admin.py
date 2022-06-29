from django.contrib import admin

from pacientes.models import Paciente
from datetime import date

# Register your models here.


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display =['nombre_completo','dni','telefono', 'edad']

    def nombre_completo(self, obj):
        return obj.nombre + ' ' + obj.apellido

     
    def edad(self,obj):
        hoy= date.today()
        años= hoy.year - obj.fecha_de_nacimiento.year -((hoy.month, hoy.day) <
        (obj.fecha_de_nacimiento.month, obj.fecha_de_nacimiento.day))
        return años



    