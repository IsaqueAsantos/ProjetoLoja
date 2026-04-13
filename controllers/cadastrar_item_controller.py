import json
import os
import shutil

class CadastrarItemController:
    def __init__(self, path="data/itens.json", images_dir="assets/images/itens"):
        self.path = path
        self.images_dir = images_dir
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

    def copiar_imagem(self, src_path: str) -> str:
        """
        Copia a imagem selecionada para assets/images/itens/
        e retorna o caminho relativo salvo no JSON.
        """
        os.makedirs(self.images_dir, exist_ok=True)

        ext = os.path.splitext(src_path)[1]           # ex: .png, .jpg
        novo_id = self.gerar_id()
        nome_arquivo = f"item_{novo_id}{ext}"
        dest_path = os.path.join(self.images_dir, nome_arquivo)

        shutil.copy2(src_path, dest_path)

        # caminho relativo para salvar no JSON e usar no ft.Image
        return dest_path.replace("\\", "/")

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