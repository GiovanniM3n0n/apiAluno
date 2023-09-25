from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle.models import Tarefas
from controle.serializers.tarefasSerializer import TarefasSerializer

class AlunoTarefaListView(APIView):
    serializer_class = TarefasSerializer

    def get(self, request, aluno_id):
        queryset = Tarefas.objects.filter(aluno_id=aluno_id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
 