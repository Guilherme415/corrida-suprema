import pygame

class Texto:
    def __init__(self, texto, fonte, cor=(255,255,255)):
        self.texto = texto
        self.fonte = fonte
        self.cor = cor

    def desenhar(self, tela, pos, centro=False):
        img = self.fonte.render(self.texto, True, self.cor)
        rect = img.get_rect()
        rect.center = pos if centro else rect.topleft
        tela.blit(img, rect)

class Botao:
    def __init__(self, texto, rect, fonte):
        self.texto = texto
        self.rect = pygame.Rect(rect)
        self.fonte = fonte

    def desenhar(self, tela):
        mouse = pygame.mouse.get_pos()
        cor = (70,70,85) if self.rect.collidepoint(mouse) else (50,50,65)
        pygame.draw.rect(tela, cor, self.rect, border_radius=12)
        pygame.draw.rect(tela, (230,230,230), self.rect, 2, border_radius=12)
        img = self.fonte.render(self.texto, True, (255,255,255))
        tela.blit(img, img.get_rect(center=self.rect.center))

    def clicou(self, evento):
        return (
            evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
            and self.rect.collidepoint(evento.pos)
        )
