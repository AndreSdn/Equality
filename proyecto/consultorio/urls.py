from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from pacientes.views import PacienteViewSet


router = routers.DefaultRouter()
router.register('', PacienteViewSet)

urlpatterns = [
    path('admin/',admin.site.urls),
    path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
