from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle.models import Tarefas
from controle.serializers.tarefasSerializer import TarefasSerializer
from django.http import Http404

class TarefaRetrieveUpdateDeleteView(APIView):
    serializer_class = TarefasSerializer

    def get_object(self, pk):
        try:
            return Tarefas.objects.get(pk=pk)
        except Tarefas.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = self.serializer_class(tarefa)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        tarefa = self.get_object(pk)
        serializer = self.serializer_class(tarefa, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        tarefa = self.get_object(pk)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
