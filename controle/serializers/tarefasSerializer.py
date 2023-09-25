from rest_framework import serializers
from controle.models.tarefas import Tarefas

class TarefasSerializer(serializers.ModelSerializer):
    disciplinas = serializers.StringRelatedField
    aluno = serializers.StringRelatedField

    class Meta:
        model = Tarefas
        fields = '__all__'