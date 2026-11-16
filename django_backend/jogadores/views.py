import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Jogador


@csrf_exempt
def salvar_pontuacao(request):
    if request.method != "POST":
        return JsonResponse({"erro": "Use POST"}, status=405)

    try:
        dados = json.loads(request.body.decode("utf-8"))
        jogador = Jogador.objects.create(
            nome=str(dados.get("nome", "Jogador"))[:100],
            pontuacao=max(0, int(dados.get("pontuacao", 0))),
            cor_carro=str(dados.get("cor_carro", "vermelho"))[:20],
            fases_vencidas=max(0, int(dados.get("fases_vencidas", 0)))
        )
        return JsonResponse({"ok": True, "id": jogador.id})
    except Exception as erro:
        return JsonResponse({"ok": False, "erro": str(erro)}, status=400)


def ranking(request):
    dados = list(
        Jogador.objects.order_by("-pontuacao", "-fases_vencidas").values(
            "nome", "pontuacao", "cor_carro", "fases_vencidas"
        )[:10]
    )
    return JsonResponse({"ranking": dados})