import pygame
from .recursos import carregar


class Pista:

    def __init__(self):

        self.imagem = carregar(
            "pista.png",
            (1000, 650)
        )

        self.offset = 0

        # Posição da linha de chegada
        self.linha_chegada = 120

    def atualizar(self, velocidade):

        self.offset = (
            self.offset + velocidade
        ) % 80

    def desenhar(self, tela):

        if self.imagem:

            tela.blit(
                self.imagem,
                (0, 0)
            )

        else:

            tela.fill(
                (35, 145, 65)
            )

            pygame.draw.rect(
                tela,
                (70, 70, 70),
                (210, 0, 580, 650)
            )

            pygame.draw.line(
                tela,
                (255, 255, 255),
                (210, 0),
                (210, 650),
                5
            )

            pygame.draw.line(
                tela,
                (255, 255, 255),
                (790, 0),
                (790, 650),
                5
            )

            # Faixas centrais
            for x in (395, 605):

                y = -80 + self.offset

                while y < 650:

                    pygame.draw.rect(
                        tela,
                        (245, 245, 245),
                        (x, y, 10, 45)
                    )

                    y += 80

            # Faixas laterais
            for y in range(-40, 650, 80):

                yy = y + self.offset

                pygame.draw.rect(
                    tela,
                    (230, 230, 230),
                    (
                        210,
                        yy,
                        18,
                        40
                    )
                )

                pygame.draw.rect(
                    tela,
                    (230, 230, 230),
                    (
                        772,
                        yy,
                        18,
                        40
                    )
                )

        # -------------------------
        # LINHA DE CHEGADA
        # -------------------------

        tamanho = 40

        for x in range(
            220,
            780,
            tamanho
        ):

            if (x // tamanho) % 2 == 0:
                cor = (255, 255, 255)
            else:
                cor = (20, 20, 20)

            pygame.draw.rect(
                tela,
                cor,
                (
                    x,
                    self.linha_chegada,
                    tamanho,
                    25
                )
            )

        # Texto da chegada
        fonte = pygame.font.Font(
            None,
            25
        )

        texto = fonte.render(
            "CHEGADA",
            True,
            (255, 255, 255)
        )

        tela.blit(
            texto,
            (
                470,
                self.linha_chegada - 32
            )
        )