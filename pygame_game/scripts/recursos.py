import os
import pygame

BASE = os.path.dirname(os.path.dirname(__file__))
ASSETS = os.path.join(BASE, "assets")

def carregar(nome, tamanho):
    caminho = os.path.join(ASSETS, nome)
    if os.path.exists(caminho):
        try:
            imagem = pygame.image.load(caminho).convert_alpha()
            return pygame.transform.smoothscale(imagem, tamanho)
        except pygame.error:
            return None
    return None
