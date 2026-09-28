import pygame
from .config import CORES_CARRO
from .recursos import carregar


class Carro:

    def __init__(
        self,
        x,
        y,
        cor="vermelho",
        jogador=True
    ):

        self.rect = pygame.Rect(
            x,
            y,
            48,
            82
        )

        self.cor = cor
        self.jogador = jogador

        # Velocidade lateral
        self.velocidade = 6

        self.imagem = carregar(
            "carro.png"
            if jogador
            else "adversario.png",
            self.rect.size
        )

    def atualizar_jogador(self, teclas):

        if not self.jogador:
            return

        esquerda = (
            teclas[pygame.K_LEFT]
            or teclas[pygame.K_a]
        )

        direita = (
            teclas[pygame.K_RIGHT]
            or teclas[pygame.K_d]
        )

        if esquerda:
            self.rect.x -= self.velocidade

        if direita:
            self.rect.x += self.velocidade

        # Limites da pista
        self.rect.left = max(
            220,
            self.rect.left
        )

        self.rect.right = min(
            780,
            self.rect.right
        )

    def atualizar_adversario(self, velocidade):

        if self.jogador:
            return

        # Agora o movimento do adversário
        # é controlado pela Fase.
        self.rect.y -= velocidade

    def desenhar(self, tela):

        if self.imagem:

            tela.blit(
                self.imagem,
                self.rect
            )

            return

        # Caso a imagem não seja encontrada,
        # desenha um carro simples.

        cor = CORES_CARRO.get(
            self.cor,
            CORES_CARRO["vermelho"]
        )

        pygame.draw.rect(
            tela,
            cor,
            self.rect,
            border_radius=10
        )

        pygame.draw.rect(
            tela,
            (35, 35, 45),
            (
                self.rect.x + 8,
                self.rect.y + 13,
                32,
                30
            ),
            border_radius=7
        )

        pygame.draw.rect(
            tela,
            (190, 220, 240),
            (
                self.rect.x + 12,
                self.rect.y + 17,
                24,
                20
            ),
            border_radius=5
        )

        pygame.draw.circle(
            tela,
            (20, 20, 20),
            (
                self.rect.left + 8,
                self.rect.bottom - 8
            ),
            6
        )

        pygame.draw.circle(
            tela,
            (20, 20, 20),
            (
                self.rect.right - 8,
                self.rect.bottom - 8
            ),
            6
        )