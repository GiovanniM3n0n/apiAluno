from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle.models import Disciplina
from controle.serializers.disciplinaSerializer import DisciplinaSerializer
from django.http import Http404

class DisciplinaRetrieveUpdateDeleteView(APIView):
    serializer_class = DisciplinaSerializer

    def get_object(self, pk):
        try:
            return Disciplina.objects.get(pk=pk)
        except Disciplina.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = self.serializer_class(disciplina)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        disciplina = self.get_object(pk)
        serializer = self.serializer_class(disciplina, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        disciplina = self.get_object(pk)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)