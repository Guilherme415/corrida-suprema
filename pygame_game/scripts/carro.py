
import pygame
from .recursos import carregar


ARQUIVOS_VEICULOS = {
    "Carro": ["carro1.png", "carro2.png"],
    "Moto": ["moto1.png", "moto2.png"],
    "Caminhão": ["caminhao1.png", "caminhao2.png"],
    "Bicicleta": ["bicicleta1.png", "bicicleta2.png"],
    "Ônibus": ["onibus1.png", "onibus2.png"]
}


class Carro:

    def __init__(
        self,
        x,
        y,
        veiculo="Carro",
        jogador=True,
        numero_imagem=0
    ):

        self.rect = pygame.Rect(
            x,
            y,
            48,
            82
        )

        self.cor = veiculo
        self.jogador = jogador

        self.velocidade = 6
        self.parado_ate = 0

        arquivos = ARQUIVOS_VEICULOS.get(
            veiculo,
            ARQUIVOS_VEICULOS["Carro"]
        )

        numero_imagem = numero_imagem % len(arquivos)

        self.imagem = carregar(
            arquivos[numero_imagem],
            self.rect.size
        )

    def atualizar_jogador(self, teclas):

        if not self.jogador:
            return

        agora = pygame.time.get_ticks()

        if agora < self.parado_ate:
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

        self.rect.left = max(
            220,
            self.rect.left
        )

        self.rect.right = min(
            780,
            self.rect.right
        )

    def parar_por_2_segundos(self):

        self.parado_ate = (
            pygame.time.get_ticks() + 2000
        )

    def esta_parado(self):

        return pygame.time.get_ticks() < self.parado_ate

    def atualizar_adversario(self, velocidade):

        if self.jogador:
            return

        self.rect.y -= velocidade

    def desenhar(self, tela):

        if self.imagem:
            tela.blit(
                self.imagem,
                self.rect
            )