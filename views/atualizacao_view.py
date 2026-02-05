import flet as ft
from ui.theme import *


class AtualizacoesView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            alignment=ft.Alignment(0, -0.9),
            content=ft.Column(
                width=720,
                spacing=32,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    # ===== HEADER =====
                    ft.Row(
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
                                on_click=lambda e: self.app.show_view("HomeView"),
                            ),
                            ft.Container(width=8),
                            ft.Text(
                                "Atualizações",
                                size=22,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT_PRIMARY,
                            ),
                        ],
                    ),

                    # ===== CARD VERSÃO =====
                    ft.Container(
                        width=620,
                        padding=32,
                        border_radius=18,
                        bgcolor=BG_CARD,
                        content=ft.Column(
                            spacing=22,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    width=64,
                                    height=64,
                                    border_radius=16,
                                    bgcolor=PRIMARY,
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Icon(
                                        ft.Icons.SYNC,
                                        size=30,
                                        color=ft.Colors.WHITE,
                                    ),
                                ),
                                ft.Column(
                                    spacing=4,
                                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.Text(
                                            "Versão 1.0.0",
                                            size=20,
                                            weight=ft.FontWeight.BOLD,
                                            color=TEXT_PRIMARY,
                                        ),
                                        ft.Text(
                                            "Sistema de Pedidos",
                                            size=14,
                                            color=TEXT_MUTED,
                                        ),
                                    ],
                                ),
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        spacing=10,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.Icons.REFRESH,
                                                size=18,
                                                color=ft.Colors.WHITE,
                                            ),
                                            ft.Text(
                                                "Verificar Atualizações",
                                                size=15,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.WHITE,
                                            ),
                                        ],
                                    ),
                                    bgcolor=PRIMARY,
                                    height=48,
                                    width=420,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=14),
                                    ),
                                    on_click=self._check_updates,
                                ),
                            ],
                        ),
                    ),

                    # ===== NOTAS =====
                    ft.Column(
                        width=620,
                        spacing=16,
                        controls=[
                            ft.Text(
                                "NOTAS DE VERSÃO",
                                size=13,
                                weight=ft.FontWeight.BOLD,
                                color=TEXT_MUTED,
                            ),

                            ft.Container(
                                padding=24,
                                border_radius=16,
                                bgcolor=BG_CARD,
                                content=ft.Column(
                                    spacing=18,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                            controls=[
                                                ft.Text(
                                                    "Versão 1.0.0",
                                                    size=16,
                                                    weight=ft.FontWeight.BOLD,
                                                    color=TEXT_PRIMARY,
                                                ),
                                                ft.Text(
                                                    "05/02/2026",
                                                    size=13,
                                                    color=TEXT_MUTED,
                                                ),
                                            ],
                                        ),

                                        self._note_item(
                                            ft.Icons.ROCKET_LAUNCH,
                                            "Lançamento inicial do sistema",
                                        ),
                                        self._note_item(
                                            ft.Icons.SHIELD_OUTLINED,
                                            "Gestão completa de pedidos",
                                        ),
                                        self._note_item(
                                            ft.Icons.BOLT,
                                            "Cadastro de itens com categorias",
                                        ),
                                    ],
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

    # ===== ITEM DA LISTA =====
    def _note_item(self, icon, text):
        return ft.Row(
            spacing=14,
            controls=[
                ft.Container(
                    width=36,
                    height=36,
                    border_radius=10,
                    bgcolor=PRIMARY + "33",
                    alignment=ft.Alignment(0, 0),
                    content=ft.Icon(icon, size=18, color=PRIMARY),
                ),
                ft.Text(
                    text,
                    size=14,
                    color=TEXT_PRIMARY,
                    expand=True,
                ),
            ],
        )

    # ===== AÇÃO =====
    def _check_updates(self, e):
        print("Verificando atualizações...")
