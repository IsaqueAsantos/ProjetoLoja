import json
from pathlib import Path

def carregar_itens():
    caminho = Path("data/itens.json")

    if not caminho.exists():
        return []

    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)
