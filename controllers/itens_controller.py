import json
from pathlib import Path

class ItensController:
    def __init__(self, path="data/itens.json"):
        self.path = Path(path)

    def _load(self):
        if not self.path.exists():
            return []
        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def excluir_item(self, item_id: int):
        data = self._load()
        data = [i for i in data if i["id"] != item_id]
        self._save(data)

    def editar_item(self, item_id: int, nome: str, valor: float, categoria: str):
        data = self._load()
        for item in data:
            if item["id"] == item_id:
                item["nome"] = nome
                item["valor"] = float(valor)
                item["categoria"] = categoria
                break
        self._save(data)