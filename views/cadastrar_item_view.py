import flet as ft
from ui.theme import *


class CadastrarView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            alignment=ft.Alignment(0, -0.9),
            content=ft.Column(
                width=720,
                spacing=24,
                controls=[
                    # ===== HEADER =====
                    ft.Row(
                        width=720,
                        alignment=ft.MainAxisAlignment.START,
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
                                on_click=lambda e: self.app.show_view("HomeView"),
                            ),
                            ft.Container(width=16),
                            ft.Text(
                                "Cadastrar Item",
                                style=font_header(),
                                color=TEXT_PRIMARY,
                            ),
                        ],
                    ),

                    # ===== CARD =====
                    ft.Container(
                        width=700,
                        padding=24,
                        border_radius=20,
                        bgcolor=BG_CARD,
                        content=ft.Column(
                            spacing=16,
                            controls=[
                                # Imagem
                                ft.Text(
                                    "Imagem do Produto",
                                    style=font_label(),
                                    color=TEXT_SECONDARY,
                                ),
                                ft.Row(
                                    spacing=12,
                                    controls=[
                                        ft.Container(
                                            width=96,
                                            height=96,
                                            border_radius=16,
                                            bgcolor=BG_CARD_HOVER,
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Row(
                                                spacing=8,
                                                controls=[
                                                    ft.Icon(
                                                        ft.Icons.UPLOAD,
                                                        color=TEXT_MUTED,
                                                        size=18,
                                                    ),
                                                    ft.Text(
                                                        "Fazer upload",
                                                        style=font_text(),
                                                        color=TEXT_MUTED,
                                                    ),
                                                ],
                                            ),
                                            height=96,
                                            expand=True,
                                            bgcolor=BG_CARD_HOVER,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=16),
                                            ),
                                            on_click=self._upload_image,
                                        ),
                                    ],
                                ),

                                # Nome
                                ft.Text(
                                    "Nome *",
                                    style=font_label(),
                                    color=TEXT_SECONDARY,
                                ),
                                ft.TextField(
                                    height=44,
                                    border_radius=14,
                                    hint_text="Ex: X-Burger",
                                    bgcolor=BG_CARD_HOVER,
                                    color=TEXT_PRIMARY,
                                    hint_style=ft.TextStyle(color=TEXT_MUTED),
                                    border_color=BG_CARD_HOVER,
                                ),

                                # Descrição
                                ft.Text(
                                    "Descrição",
                                    style=font_label(),
                                    color=TEXT_SECONDARY,
                                ),
                                ft.TextField(
                                    multiline=True,
                                    min_lines=3,
                                    max_lines=3,
                                    border_radius=14,
                                    bgcolor=BG_CARD_HOVER,
                                    color=TEXT_PRIMARY,
                                    border_color=BG_CARD_HOVER,
                                ),

                                # Preço + Categoria
                                ft.Row(
                                    spacing=8,
                                    controls=[
                                        ft.TextField(
                                            hint_text="0,00",
                                            height=44,
                                            expand=True,
                                            border_radius=14,
                                            bgcolor=BG_CARD_HOVER,
                                            color=TEXT_PRIMARY,
                                            hint_style=ft.TextStyle(color=TEXT_MUTED),
                                            border_color=BG_CARD_HOVER,
                                        ),
                                        ft.Dropdown(
                                            expand=True,
                                            height=44,
                                            border_radius=14,
                                            bgcolor=BG_CARD_HOVER,
                                            color=TEXT_PRIMARY,
                                            options=[
                                                ft.dropdown.Option("Cigarro"),
                                                ft.dropdown.Option("Cancer"),
                                                ft.dropdown.Option("Pênis"),
                                            ],
                                        ),
                                    ],
                                ),

                                # Botão salvar
                                ft.ElevatedButton(
                                    content=ft.Row(
                                        spacing=8,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        controls=[
                                            ft.Icon(
                                                ft.Icons.SAVE,
                                                color=ft.Colors.WHITE,
                                                size=18,
                                            ),
                                            ft.Text(
                                                "Cadastrar Item",
                                                style=font_button(),
                                                color=TEXT_PRIMARY,
                                            ),
                                        ],
                                    ),
                                    height=48,
                                    bgcolor=PRIMARY,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=18)
                                    ),
                                    on_click=self._save_item,
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )

    # ===== ACTIONS =====

    def _upload_image(self, e):
        print("Upload de imagem")

    def _save_item(self, e):
        print("Cadastrar item")
