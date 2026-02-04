import flet as ft
from ui.theme import *

class NovoPedidoView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            padding=20,
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
                                width=42,
                                height=36,
                                style=ft.ButtonStyle(
                                    shape=ft.RoundedRectangleBorder(radius=12)
                                ),
                                on_click=lambda e: self.app.show_view("PedidosView"),
                            ),
                            ft.Container(width=12),
                            ft.Text(
                                "Novo Pedido",
                                style=font_header(),
                                color=TEXT_PRIMARY,
                            ),
                        ],
                    ),

                    ft.Container(height=24),

                    # ================= CONTEÚDO =================
                    ft.Column(
                        expand=True,
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            # ===== FORM =====
                            ft.Column(
                                width=420,
                                horizontal_alignment=ft.CrossAxisAlignment.START,
                                controls=[
                                    ft.Text(
                                        "Nome do Cliente",
                                        style=font_label(),
                                        color=TEXT_PRIMARY,
                                    ),
                                    ft.TextField(
                                        height=44,
                                        hint_text="Digite o nome do cliente",
                                        bgcolor=BG_CARD,
                                        color=TEXT_PRIMARY,
                                        hint_style=ft.TextStyle(
                                            color=TEXT_MUTED
                                        ),
                                        border_radius=14,
                                        border_color=BG_CARD,
                                    ),
                                ],
                            ),

                            ft.Container(height=40),

                            # ===== ESTADO VAZIO =====
                            ft.Column(
                                expand=True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Text(
                                        "📦",
                                        size=32,
                                    ),
                                    ft.Container(height=8),
                                    ft.Text(
                                        "Nenhum item cadastrado",
                                        style=font_text(),
                                        color=TEXT_MUTED,
                                    ),
                                    ft.Container(height=14),
                                    ft.ElevatedButton(
                                        content=ft.Text(
                                            "Cadastrar Item",
                                            color=TEXT_PRIMARY,
                                            weight=ft.FontWeight.BOLD,
                                        ),
                                        width=180,
                                        height=44,
                                        style=ft.ButtonStyle(
                                            bgcolor={
                                                ft.ControlState.DEFAULT: PRIMARY,
                                                ft.ControlState.HOVERED: PRIMARY_HOVER,
                                            },
                                            shape=ft.RoundedRectangleBorder(radius=18),
                                        ),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
