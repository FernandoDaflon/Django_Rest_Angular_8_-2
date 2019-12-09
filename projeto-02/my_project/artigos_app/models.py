from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=255)
    site = models.URLField(blank=True, null=True)
    email = models.EmailField()

    def __str__(self):
        return '{}'.format(self.nome)

class Artigo(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    publicado_em = models.DateField(auto_now=True)
    atualizado_em = models.DateField(auto_now=True)
    texto = models.TextField()

    def __str__(self):
        return '{}'.format(self.titulo)
