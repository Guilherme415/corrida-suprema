import json
import urllib.request

BASE = "http://127.0.0.1:8000"

def salvar(nome, pontuacao, cor, fases):
    try:
        dados = json.dumps({
            "nome": nome,
            "pontuacao": pontuacao,
            "cor_carro": cor,
            "fases_vencidas": fases
        }).encode()
        req = urllib.request.Request(
            BASE + "/api/salvar/",
            data=dados,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=2) as r:
            return r.status == 200
    except Exception:
        return False

def buscar_ranking():
    try:
        with urllib.request.urlopen(BASE + "/api/ranking/", timeout=2) as r:
            return json.loads(r.read().decode()).get("ranking", [])
    except Exception:
        return []
