from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle.models import Disciplina
from controle.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

