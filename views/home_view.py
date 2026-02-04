import flet as ft

from ui.theme import *
from ui.components import primary_button


class HomeView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Text("Sistema de Pedidos", style=font_title()),
                    ft.Container(height=32),

                    primary_button(
                        text="Novo Pedido",
                        icon=ft.Icons.ADD_SHOPPING_CART_OUTLINED,
                        on_click=lambda e: self.app.show_view("PedidosView"),
                    ),

                    ft.Container(height=16),

                    primary_button(
                        text="Itens Cadastrados",
                        icon=ft.Icons.LIST_ALT,
                        on_click=lambda e: self.app.show_view("ItensView"),
                    ),
                ],
            ),
        )
