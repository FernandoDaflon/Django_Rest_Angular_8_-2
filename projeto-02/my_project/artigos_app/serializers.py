from .models import Autor, Artigo
from rest_framework import serializers

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'

class ArtigoSerializer(serializers.ModelSerializer):
    autor = AutorSerializer()
    class Meta:
        model = Artigo
        fields = ('titulo','publicado_em','atualizado_em','texto','autor')
        #
        # ('titulo', 'publicado_em', 'atualizadp_em', 'texto', 'autor')
            # '__all__'