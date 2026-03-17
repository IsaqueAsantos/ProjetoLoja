import json
import os

class CadastrarItemController:
    def __init__(self, path="data/itens.json"):
        self.path = path
        self.data = self._load()

    def _load(self):
        if not os.path.exists(self.path):
            return []

        with open(self.path, "r", encoding="utf-8") as f:
            return json.load(f)

    def _save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

    def gerar_id(self):
        if not self.data:
            return 1
        return max(item["id"] for item in self.data) + 1

    def validar(self, nome, valor, categoria):
        if not nome or not valor or not categoria:
            return False, "Preencha todos os campos"

        try:
            float(valor)
        except:
            return False, "Valor inválido"

        return True, ""

    def salvar_item(self, nome, valor, categoria, imagem):
        novo_item = {
            "id": self.gerar_id(),
            "nome": nome,
            "valor": float(valor),
            "categoria": categoria,
            "imagem": imagem
        }

        self.data.append(novo_item)
        self._save()

        return novo_item