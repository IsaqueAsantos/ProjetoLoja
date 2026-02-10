class NovoPedidoController:
    def __init__(self, itens):
        self.itens = itens
        self.carrinho = {}
        self.desconto = 0.0
        self.search_text = ""

    # ========= BUSCA =========
    def set_search(self, text: str):
        self.search_text = text.lower().strip()

    def get_itens_filtrados(self):
        if not self.search_text:
            return self.itens
        return [
            item for item in self.itens
            if self.search_text in item["nome"].lower()
        ]

    # ========= CARRINHO =========
    def add_item(self, item_id):
        self.carrinho[item_id] = self.carrinho.get(item_id, 0) + 1

    def remove_item(self, item_id):
        qtd = self.carrinho.get(item_id, 0)
        if qtd > 1:
            self.carrinho[item_id] -= 1
        elif qtd == 1:
            del self.carrinho[item_id]

    def get_qtd(self, item_id):
        return self.carrinho.get(item_id, 0)

    # ========= DESCONTO =========
    def set_desconto(self, valor: float):
        self.desconto = max(0.0, min(valor, 100.0))

    def get_desconto(self):
        return self.desconto

    # ========= CÁLCULOS =========
    def calcular_subtotal(self):
        return sum(
            (item["valor"] - item.get("desconto", 0)) * self.carrinho.get(item["id"], 0)
            for item in self.itens
        )

    def calcular_total(self):
        subtotal = self.calcular_subtotal()
        return round(subtotal * (1 - self.desconto / 100), 2)

    # ========= RESUMO =========
    def get_resumo(self):
        resumo = []
        for item in self.itens:
            qtd = self.carrinho.get(item["id"], 0)
            if qtd:
                subtotal_item = (item["valor"] - item.get("desconto", 0)) * qtd
                resumo.append({
                    "nome": item["nome"],
                    "qtd": qtd,
                    "subtotal": round(subtotal_item, 2),
                })
        return resumo

    # ========= RESET =========
    def limpar(self):
        self.carrinho.clear()
        self.desconto = 0.0
