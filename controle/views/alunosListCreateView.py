from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from controle.models.aluno import Aluno
from controle.serializers.alunoSerializer import AlunoSerializer

class AlunoListCreateView(APIView):
    def get(self, request):
        alunos = Aluno.objects.all()
        serializer = AlunoSerializer(alunos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AlunoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
