from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    profissao = models.CharField(max_length=200)
    ano_nasc = models.PositiveIntegerField(validators=[MinValueValidator(1970), MaxValueValidator(datetime.now().year)])
    ativo = models.BooleanField(default=True)



    def __str__(self):
        return "{}".format(self.nome)

            # "{}".format(self.nome) + " " + "{}".format(self.profissao) + " " + "{}".format(self.ativo)


            # "{} + ' ' +  {} + ' ' + {}".format(self.nome, self.profissao, self.ativo)

            # self.nome + ' ' + self.profissao + '' + self.ativo

