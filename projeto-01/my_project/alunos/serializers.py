from rest_framework import serializers

# from aluno.models import Aluno
from .models import Aluno


class AlunoSerzializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
