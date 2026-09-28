# 🏎️ Corrida 5 Fases — Pygame + Django

Jogo de corrida 2D desenvolvido em Pygame, com integração com Django.

## Critérios do trabalho
- 5 fases
- Pontuação
- Ranking
- Personagem/jogador
- Adversário
- Cenário
- Regras e dinâmica
- Escolha da cor do carro
- Integração com Django para armazenar jogadores e pontuações

## Como funciona
O jogador controla um carro e precisa chegar à linha de chegada antes do adversário.
A cada fase, o adversário fica mais rápido, aumentando a dificuldade.

### Fases
1. Fácil — adversário lento
2. Normal — adversário um pouco mais rápido
3. Difícil
4. Muito difícil
5. Final — adversário mais rápido

## Controles
- ← / → ou A / D: mover o carro
- ENTER: iniciar
- ESC: voltar ao menu
- No menu: clique nos botões
- Clique nas cores para escolher o carro

## Pontuação
Quanto mais rápido você terminar, mais pontos recebe.
Vencer a fase dá bônus.
Completar todas as 5 fases gera uma pontuação final enviada ao Django.

## Imagens
Coloque suas imagens em `pygame_game/assets/`:
- carro.png
- adversario.png
- pista.png
- fundo.png
- trofeu.png

Se as imagens não existirem, o jogo cria desenhos simples automaticamente.

## Django
Em um terminal:
```bash
cd django_backend
python manage.py migrate
python manage.py runserver
```

Em outro terminal:
```bash
cd pygame_game
python main.py
```

O ranking é salvo no banco SQLite do Django.
