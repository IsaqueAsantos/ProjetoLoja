class PedidoController:
    def __init__(self, itens):
        self.itens = itens
        self.carrinho = {}  # {id: qtd}

    def add_item(self, item_id):
        self.carrinho[item_id] = self.carrinho.get(item_id, 0) + 1

    def remove_item(self, item_id):
        if item_id in self.carrinho:
            self.carrinho[item_id] -= 1
            if self.carrinho[item_id] <= 0:
                del self.carrinho[item_id]

    def get_qtd(self, item_id):
        return self.carrinho.get(item_id, 0)

    def get_total(self):
        total = 0
        for item in self.itens:
            qtd = self.carrinho.get(item["id"], 0)
            if qtd:
                total += (item["valor"] - item.get("desconto", 0)) * qtd
        return total
