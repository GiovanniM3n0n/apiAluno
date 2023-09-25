
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from controle.models import Disciplina
from controle.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaListCreateView(APIView):
    serializer_class = DisciplinaSerializer

    def get(self, request):
        queryset = Disciplina.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)