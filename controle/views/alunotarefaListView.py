from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from controle.models import Tarefas
from controle.serializers.tarefasSerializer import TarefasSerializer

class AlunoTarefaListView(generics.ListAPIView):
    serializer_class = TarefasSerializer

    def get_queryset(self):
        aluno_id = self.kwargs['aluno_id']
        return Tarefas.objects.filter(aluno_id=aluno_id)
    
 