from django.db import models
#as informações de piloto disponiveis
class Piloto(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.PositiveBigIntegerField()
    classificacao = models.PositiveBigIntegerField()
    equipe = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.nome} está na {self.classificacao} posicao'

#as informações de carro disponíveis
class Carro (models.Model):
    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    velocidade_maxima = models.PositiveBigIntegerField()
    escolha_cores = (
        ('VERMELHO', 'Vermelho'),
        ('ROSA', 'Rosa'),
        ('BRANCO', 'Branco'),
        ('PRETO', 'Preto'),
        ('ROXO', 'Roxo')
    )
    cor = models.CharField(max_length=50)
    piloto = models.ForeignKey(Piloto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} é da cor {self.cor}'
