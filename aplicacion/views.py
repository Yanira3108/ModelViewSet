from rest_framework.viewsets import ModelViewSet
from apps.post.models import Response
from rest_framework import status
from .models import Persona
# Create your views here.
class personaViewsets(ModelViewSet):
    queryset= Persona.objects.all()
    serializer_class
    