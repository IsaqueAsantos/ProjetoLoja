import flet as ft
from ui.theme import *

class PedidosView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            padding=16,
            content=ft.Column(
                expand=True,
                controls=[
                    # ================= HEADER =================
                    ft.Row(
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.ARROW_BACK_ROUNDED,
                                icon_color=TEXT_SECONDARY,
                                bgcolor=BG_CARD,
                                width=44,
                                height=36,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12)
                                ),
                                on_click=lambda e: self.app.show_view("HomeView"),
                            ),
                            ft.Container(width=12),
                            ft.Text(
                                "Pedidos Ativos",
                                style=font_header(),
                                color=TEXT_PRIMARY,
                            ),
                        ],
                    ),

                    # ================= CONTEÚDO CENTRAL =================
                    ft.Column(
                        expand=True,
                        alignment=ft.MainAxisAlignment.CENTER,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Text(
                                "Nenhum pedido ativo",
                                style=font_text(),
                                color=TEXT_MUTED,
                            ),

                            ft.Container(height=24),

                            ft.ElevatedButton(
                                content=ft.Text(
                                    "+  Novo Pedido",
                                    color=TEXT_SECONDARY,
                                    weight=ft.FontWeight.BOLD,
                                ),
                                width=290,
                                height=56,
                                on_click=lambda e: self.app.show_view("NovoPedidoView"),
                                style=ft.ButtonStyle(
                                    bgcolor={
                                        ft.ControlState.DEFAULT: BG_CARD,
                                        ft.ControlState.HOVERED: BG_CARD_HOVER,
                                    },
                                    shape=ft.RoundedRectangleBorder(radius=22),
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )
