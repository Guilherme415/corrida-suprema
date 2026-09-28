import pygame
from scripts.config import (
    LARGURA, ALTURA, FPS, CORES_CARRO, NOMES_CORES
)
from scripts.interfaces import Texto, Botao
from scripts.fase import Fase
from scripts.api import salvar, buscar_ranking

pygame.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("🏎️ Corrida 5 Fases")
clock = pygame.time.Clock()

F_TITULO = pygame.font.Font(None, 72)
F_GRANDE = pygame.font.Font(None, 50)
F_MEDIA = pygame.font.Font(None, 34)
F_PEQUENA = pygame.font.Font(None, 25)

estado = "menu"
nome = ""
cor_i = 0

fase_num = 1
pontuacao = 0
fases_vencidas = 0
tentativas = 1

fase = None
enviado = False


def menu():

    tela.fill((20, 24, 38))

    Texto(
        "CORRIDA 5 FASES",
        F_TITULO
    ).desenhar(
        tela,
        (500, 75),
        True
    )

    Texto(
        "Escolha a cor do seu carro",
        F_MEDIA
    ).desenhar(
        tela,
        (500, 145),
        True
    )

    for i, cor in enumerate(NOMES_CORES):

        rect = pygame.Rect(
            330 + i * 70,
            190,
            50,
            50
        )

        pygame.draw.rect(
            tela,
            CORES_CARRO[cor],
            rect,
            border_radius=10
        )

        if i == cor_i:

            pygame.draw.rect(
                tela,
                (255, 255, 255),
                rect,
                4,
                border_radius=10
            )

    Texto(
        "Nome: " + (nome or "Jogador"),
        F_MEDIA
    ).desenhar(
        tela,
        (500, 285),
        True
    )

    Texto(
        "Clique nesta tela e digite seu nome",
        F_PEQUENA,
        (180, 180, 190)
    ).desenhar(
        tela,
        (500, 320),
        True
    )

    b_jogar = Botao(
        "COMEÇAR",
        (350, 365, 300, 60),
        F_MEDIA
    )

    b_rank = Botao(
        "RANKING",
        (350, 445, 300, 60),
        F_MEDIA
    )

    b_jogar.desenhar(tela)
    b_rank.desenhar(tela)

    Texto(
        "ESPAÇO = acelerar | ← → / A D = dirigir",
        F_PEQUENA,
        (190, 190, 200)
    ).desenhar(
        tela,
        (500, 560),
        True
    )


def iniciar():

    global estado
    global fase

    fase = Fase(
        fase_num,
        NOMES_CORES[cor_i],
        tentativas
    )

    estado = "corrida"


def corrida():

    global estado
    global pontuacao
    global fases_vencidas

    teclas = pygame.key.get_pressed()

    fase.jogador.atualizar_jogador(teclas)
    fase.atualizar()

    fase.pista.desenhar(tela)

    fase.jogador.desenhar(tela)
    fase.adversario.desenhar(tela)

    pygame.draw.rect(
        tela,
        (15, 15, 20),
        (0, 0, LARGURA, 65)
    )

    Texto(
        f"FASE {fase_num}/5",
        F_MEDIA
    ).desenhar(
        tela,
        (25, 15)
    )

    Texto(
        f"PONTOS: {pontuacao}",
        F_MEDIA
    ).desenhar(
        tela,
        (220, 15)
    )

    Texto(
        f"TENTATIVA: {tentativas}",
        F_MEDIA
    ).desenhar(
        tela,
        (450, 15)
    )

    b_acelerar = Botao(
        "ACELERAR!",
        (350, 570, 300, 60),
        F_MEDIA
    )

    b_acelerar.desenhar(tela)

    Texto(
        "CLIQUE OU APERTE ESPAÇO O MAIS RÁPIDO QUE CONSEGUIR!",
        F_PEQUENA,
        (255, 255, 255)
    ).desenhar(
        tela,
        (500, 545),
        True
    )

    if fase.terminou:

        if fase.venceu:

            pontuacao += fase.pontos()
            fases_vencidas += 1

            estado = "vitoria"

        else:

            estado = "derrota"


def vitoria():

    tela.fill((18, 28, 35))

    Texto(
        f"FASE {fase_num} VENCIDA!",
        F_TITULO
    ).desenhar(
        tela,
        (500, 140),
        True
    )

    Texto(
        f"Você terminou na tentativa {tentativas}!",
        F_MEDIA
    ).desenhar(
        tela,
        (500, 215),
        True
    )

    Texto(
        f"Você ganhou {fase.pontos()} pontos!",
        F_GRANDE
    ).desenhar(
        tela,
        (500, 280),
        True
    )

    Texto(
        f"Pontuação total: {pontuacao}",
        F_MEDIA
    ).desenhar(
        tela,
        (500, 340),
        True
    )

    if fase_num < 5:

        b = Botao(
            "PRÓXIMA FASE",
            (350, 420, 300, 60),
            F_MEDIA
        )

        b.desenhar(tela)

    else:

        Texto(
            "Você completou as 5 fases!",
            F_MEDIA
        ).desenhar(
            tela,
            (500, 370),
            True
        )

        b = Botao(
            "FINALIZAR",
            (350, 430, 300, 60),
            F_MEDIA
        )

        b.desenhar(tela)


def derrota():

    tela.fill((35, 18, 22))

    Texto(
        "VOCÊ PERDEU!",
        F_TITULO
    ).desenhar(
        tela,
        (500, 150),
        True
    )

    Texto(
        f"FASE {fase_num} — TENTATIVA {tentativas}",
        F_GRANDE
    ).desenhar(
        tela,
        (500, 235),
        True
    )

    Texto(
        "O adversário chegou primeiro!",
        F_MEDIA
    ).desenhar(
        tela,
        (500, 300),
        True
    )

    b = Botao(
        "TENTAR NOVAMENTE",
        (350, 370, 300, 60),
        F_MEDIA
    )

    b.desenhar(tela)

    b2 = Botao(
        "VOLTAR AO MENU",
        (350, 450, 300, 60),
        F_MEDIA
    )

    b2.desenhar(tela)


def fim():

    global enviado

    tela.fill((25, 22, 38))

    Texto(
        "🏆 CORRIDA FINALIZADA!",
        F_TITULO
    ).desenhar(
        tela,
        (500, 130),
        True
    )

    Texto(
        f"{nome or 'Jogador'} — {pontuacao} pontos",
        F_GRANDE
    ).desenhar(
        tela,
        (500, 225),
        True
    )

    Texto(
        f"Fases vencidas: {fases_vencidas}/5",
        F_MEDIA
    ).desenhar(
        tela,
        (500, 285),
        True
    )

    Texto(
        "Resultado enviado para o ranking Django.",
        F_MEDIA,
        (180, 220, 180)
    ).desenhar(
        tela,
        (500, 330),
        True
    )

    if not enviado:

        enviado = salvar(
            nome or "Jogador",
            pontuacao,
            NOMES_CORES[cor_i],
            fases_vencidas
        )

    b1 = Botao(
        "VER RANKING",
        (330, 400, 340, 60),
        F_MEDIA
    )

    b2 = Botao(
        "MENU",
        (330, 480, 340, 60),
        F_MEDIA
    )

    b1.desenhar(tela)
    b2.desenhar(tela)


def ranking():

    tela.fill((20, 24, 38))

    Texto(
        "🏆 RANKING",
        F_TITULO
    ).desenhar(
        tela,
        (500, 70),
        True
    )

    dados = buscar_ranking()

    if not dados:

        Texto(
            "Nenhum resultado ainda.",
            F_MEDIA
        ).desenhar(
            tela,
            (500, 230),
            True
        )

    else:

        for i, item in enumerate(dados[:10]):  
                f"{i + 1}. " 
                f"{item['nome']} — "
                f"{item['pontuacao']} pts — "
                f"{item['fases_vencidas']}/5 fases"   
              

    Texto( 
                F_MEDIA
            ).desenhar(
                tela,
                (170, 145 + i * 40)
            )

    b = Botao(
        "VOLTAR",
        (400, 560, 200, 55),
        F_MEDIA
    )

    b.desenhar(tela)


rodando = True

while rodando:

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            rodando = False

        if evento.type == pygame.KEYDOWN:

            if estado == "menu":

                if evento.key == pygame.K_BACKSPACE:

                    nome = nome[:-1]

                elif evento.key == pygame.K_RETURN:

                    if not nome:
                        nome = "Jogador"

                    fase_num = 1
                    pontuacao = 0
                    fases_vencidas = 0
                    tentativas = 1
                    enviado = False

                    iniciar()

                elif (
                    evento.unicode.isprintable()
                    and len(nome) < 18
                ):

                    nome += evento.unicode

            elif (
                estado == "corrida"
                and evento.key == pygame.K_SPACE
            ):

                fase.acelerar()

            elif evento.key == pygame.K_ESCAPE:

                estado = "menu"

            elif (
                estado == "vitoria"
                and evento.key == pygame.K_RETURN
            ):

                if fase_num < 5:

                    fase_num += 1
                    tentativas = 1
                    iniciar()

                else:

                    estado = "fim"

            elif (
                estado == "derrota"
                and evento.key == pygame.K_RETURN
            ):

                tentativas += 1
                iniciar()

        if (
            estado == "menu"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            for i, cor in enumerate(NOMES_CORES):

                r = pygame.Rect(
                    330 + i * 70,
                    190,
                    50,
                    50
                )

                if r.collidepoint(evento.pos):

                    cor_i = i

            if pygame.Rect(
                350,
                365,
                300,
                60
            ).collidepoint(evento.pos):

                if not nome:
                    nome = "Jogador"

                fase_num = 1
                pontuacao = 0
                fases_vencidas = 0
                tentativas = 1
                enviado = False

                iniciar()

            elif pygame.Rect(
                350,
                445,
                300,
                60
            ).collidepoint(evento.pos):

                estado = "ranking"

        elif (
            estado == "corrida"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            if pygame.Rect(
                350,
                570,
                300,
                60
            ).collidepoint(evento.pos):

                fase.acelerar()

        elif (
            estado == "vitoria"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            if pygame.Rect(
                350,
                420,
                300,
                60
            ).collidepoint(evento.pos):

                if fase_num < 5:

                    fase_num += 1
                    tentativas = 1
                    iniciar()

                else:

                    estado = "fim"

            elif (
                fase_num == 5
                and pygame.Rect(
                    350,
                    430,
                    300,
                    60
                ).collidepoint(evento.pos)
            ):

                estado = "fim"

        elif (
            estado == "derrota"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            if pygame.Rect(
                350,
                370,
                300,
                60
            ).collidepoint(evento.pos):

                tentativas += 1
                iniciar()

            elif pygame.Rect(
                350,
                450,
                300,
                60
            ).collidepoint(evento.pos):

                estado = "menu"

        elif (
            estado == "fim"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            if pygame.Rect(
                330,
                400,
                340,
                60
            ).collidepoint(evento.pos):

                estado = "ranking"

            elif pygame.Rect(
                330,
                480,
                340,
                60
            ).collidepoint(evento.pos):

                estado = "menu"

        elif (
            estado == "ranking"
            and evento.type == pygame.MOUSEBUTTONDOWN
            and evento.button == 1
        ):

            if pygame.Rect(
                400,
                560,
                200,
                55
            ).collidepoint(evento.pos):

                estado = "menu"

    if estado == "menu":
        menu()

    elif estado == "corrida":
        corrida()

    elif estado == "vitoria":
        vitoria()

    elif estado == "derrota":
        derrota()

    elif estado == "fim":
        fim()

    elif estado == "ranking":
        ranking()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
