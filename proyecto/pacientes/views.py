from rest_framework import viewsets

from pacientes.models import Paciente
from .serializers import PacienteSerializer
from rest_framework import permissions


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all().order_by('nombre')
    serializer_class = PacienteSerializer
    permission_classes = [permissions.IsAuthenticated]

