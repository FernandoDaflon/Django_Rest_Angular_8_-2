from rest_framework import viewsets
from .models import Aluno
from .serializers import AlunoSerzializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all().filter(ativo=True)
    serializer_class = AlunoSerzializer