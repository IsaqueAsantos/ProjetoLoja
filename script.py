import flet as ft

from views.home_view import HomeView
from views.pedido_view import PedidosView
from views.novo_pedido_view import NovoPedidoView
from views.itens_view import ItensView
from views.atualizacao_view import AtualizacoesView
from views.cadastrar_item_view import CadastrarView
from ui.theme import BG_MAIN


class App:
    def __init__(self, page: ft.Page):
        self.page = page

        page.title = "Sistema de Pedidos"
        page.window_width = 1000
        page.window_height = 600
        page.window_resizable = True
        page.bgcolor = BG_MAIN

        self.container = ft.Container(expand=True)
        page.add(self.container)

        self.views = {
            "HomeView": HomeView(self),
            "PedidosView": PedidosView(self),
            "NovoPedidoView": NovoPedidoView(self),
            "ItensView": ItensView(self),
            "AtualizacoesView": AtualizacoesView(self),
            "CadastrarView": CadastrarView(self),
        }

        self.show_view("HomeView")

    def show_view(self, name: str):
        view = self.views[name]
        self.container.content = view.render() 
        self.page.update()


def main(page: ft.Page):
    App(page)

if __name__ == "__main__":
    ft.run(main)
