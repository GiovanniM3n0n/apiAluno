
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle.models import Tarefas
from controle.serializers.tarefasSerializer import TarefasSerializer

class TarefaListCreateView(APIView):
    serializer_class = TarefasSerializer

    def get(self, request):
        tarefas = Tarefas.objects.all()
        serializer = self.serializer_class(tarefas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
