
import pygame
from .config import VELOCIDADES_ADVERSARIO
from .carro import Carro
from .pista import Pista


class Fase:

    def __init__(
        self,
        numero,
        veiculo,
        tentativas=1
    ):

        self.numero = numero
        self.tentativas = tentativas

        self.pista = Pista()

        self.velocidade_adversario = (
            VELOCIDADES_ADVERSARIO[numero - 1]
        )

        self.jogador = Carro(
            350,
            500,
            veiculo,
            True,
            0
        )

        self.adversario = Carro(
            600,
            500,
            veiculo,
            False,
            1
        )

        self.distancia_chegada = 3000

        self.progresso_jogador = 0
        self.progresso_adversario = 0

        self.inicio = pygame.time.get_ticks()

        self.terminou = False
        self.venceu = False

        self.cliques = 0

    def acelerar(self):

        if self.terminou:
            return

        self.progresso_jogador += 35
        self.cliques += 1

        self.jogador.rect.y -= 5

    def atualizar(self):

        if self.terminou:
            return

        self.pista.atualizar(
            4 + self.numero
        )

        self.progresso_adversario += (
            self.velocidade_adversario
        )

        self.adversario.rect.y = max(
            100,
            500 - int(
                self.progresso_adversario * 0.12
            )
        )

        self.jogador.rect.y = max(
            100,
            500 - int(
                self.progresso_jogador * 0.12
            )
        )

        if self.jogador.rect.colliderect(
            self.adversario.rect
        ):

            self.terminou = True
            self.venceu = False

            return

        if self.progresso_jogador >= (
            self.distancia_chegada
        ):

            self.progresso_jogador = (
                self.distancia_chegada
            )

            self.terminou = True
            self.venceu = True

            return

        if self.progresso_adversario >= (
            self.distancia_chegada
        ):

            self.progresso_adversario = (
                self.distancia_chegada
            )

            self.terminou = True
            self.venceu = False

            return

    def tempo(self):

        return (
            pygame.time.get_ticks()
            - self.inicio
        ) / 1000

    def pontos(self):

        pontos_por_fase = {
            1: 1000,
            2: 2000,
            3: 3000,
            4: 4000,
            5: 5000
        }

        pontos_base = pontos_por_fase[
            self.numero
        ]

        if self.tentativas == 1:
            multiplicador = 1.0

        elif self.tentativas == 2:
            multiplicador = 0.7

        elif self.tentativas == 3:
            multiplicador = 0.5

        else:
            multiplicador = 0.25

        return int(
            pontos_base * multiplicador
        )

