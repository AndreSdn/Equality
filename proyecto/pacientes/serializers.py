from rest_framework import serializers
from .models import Paciente
from datetime import date

class PacienteSerializer(serializers.ModelSerializer):
    nombre_completo= serializers.SerializerMethodField ('get_nombre_completo')
    edad=serializers.SerializerMethodField('get_edad')

    class Meta:


        model = Paciente
        fields = ['nombre_completo', 'dni', 'telefono', 'edad']

    def get_nombre_completo(self, obj):
        return obj.nombre + ' ' + obj.apellido

     
    def get_edad(self,obj):
        hoy= date.today()
        años= hoy.year - obj.fecha_de_nacimiento.year -((hoy.month, hoy.day) <
        (obj.fecha_de_nacimiento.month, obj.fecha_de_nacimiento.day))
        return años