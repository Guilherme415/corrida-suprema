from django.db import models

class Jogador(models.Model):
    nome = models.CharField(max_length=100)
    pontuacao = models.IntegerField(default=0)
    cor_carro = models.CharField(max_length=20, default="vermelho")
    fases_vencidas = models.IntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-pontuacao", "criado_em"]

    def __str__(self):
        return f"{self.nome} - {self.pontuacao} pontos"
