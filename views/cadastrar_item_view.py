import flet as ft
from ui.theme import *

# ===== HELPERS =====
def Label(text):
    return ft.Text(text, style=font_label())

def Input(**kwargs):
    return ft.TextField(
        height=44,
        border_radius=14,
        bgcolor=BG_CARD_HOVER,
        border_color=BG_CARD_HOVER,
        color=TEXT_PRIMARY,
        hint_style=ft.TextStyle(color=TEXT_MUTED),
        **kwargs
    )

def DropdownField(options):
    return ft.Dropdown(
        height=44,
        border_radius=14,
        bgcolor=BG_CARD_HOVER,
        border_color=BG_CARD_HOVER,
        color=TEXT_PRIMARY,
        options=[ft.dropdown.Option(o) for o in options],
    )


class CadastrarView:
    def __init__(self, app):
        self.app = app

    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            alignment=ft.alignment.Alignment(0, 0),  # centralização geral
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,  # centraliza vertical
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=24,
                controls=[

                    # WRAPPER RESPONSIVO
                    ft.Container(
                        width=None,
                        alignment=ft.alignment.Alignment(0, 0),
                        padding=ft.padding.symmetric(horizontal=16),
                        content=ft.Column(
                            width=350,
                            spacing=24,
                            controls=[

                                # HEADER
                                ft.Row(
                                    expand=True,
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
                                        ft.Text("Cadastrar Item", style=font_header()),
                                    ],
                                ),

                                # CARD CENTRALIZADO
                                ft.Container(
                                    alignment=ft.alignment.Alignment(0, 0),
                                    content=ft.Container(
                                        width=None,
                                        padding=24,
                                        border_radius=20,
                                        bgcolor=BG_CARD,
                                        content=ft.Column(
                                            spacing=30,
                                            controls=[

                                                Label("Imagem do Produto"),

                                                ft.Row(
                                                    spacing=12,
                                                    controls=[
                                                        ft.Container(
                                                            width=124,
                                                            height=124,
                                                            border_radius=16,
                                                            bgcolor=BG_CARD_HOVER,
                                                            alignment=ft.alignment.Alignment(0, 0),
                                                            content=ft.Icon(
                                                                ft.Icons.IMAGE,
                                                                color=TEXT_MUTED
                                                            ),
                                                        ),
                                                        ft.ElevatedButton(
                                                            height=124,
                                                            width=165,
                                                            bgcolor=BG_CARD_HOVER,
                                                            style=ft.ButtonStyle(
                                                                shape=ft.RoundedRectangleBorder(radius=16),
                                                            ),
                                                            #on_click=self._upload_image,
                                                            content=ft.Row(
                                                                spacing=8,
                                                                controls=[
                                                                    ft.Icon(ft.Icons.UPLOAD, color=TEXT_MUTED, size=18),
                                                                    ft.Text("Fazer upload", style=font_text()),
                                                                ],
                                                            ),
                                                        ),
                                                    ],
                                                ),

                                                Label("Nome *"),
                                                Input(hint_text="Ex: Rothmans Blue Maço"),

                                                ft.Row(
                                                    spacing=12,
                                                    controls=[
                                                        ft.Column(
                                                            spacing=6,
                                                            width=140,
                                                            controls=[
                                                                Label("Valor *"),
                                                                Input(hint_text="R$ 0,00"),
                                                            ],
                                                        ),
                                                        ft.Column(
                                                            expand=True,
                                                            spacing=6,
                                                            controls=[
                                                                Label("Categoria *"),
                                                                DropdownField([
                                                                    "Bebida",
                                                                    "Nacional",
                                                                    "Paraguai",
                                                                    "Comida",
                                                                    "Material",
                                                                    "Outros"
                                                                ]),
                                                            ],
                                                        ),
                                                    ],
                                                ),

                                                ft.ElevatedButton(
                                                    height=48,
                                                    width=300,
                                                    bgcolor=PRIMARY,
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=18)
                                                    ),
                                                    #on_click=self._save_item,
                                                    content=ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        spacing=8,
                                                        controls=[
                                                            ft.Icon(ft.Icons.SAVE, color=ft.Colors.WHITE, size=18),
                                                            ft.Text("Cadastrar Item", style=font_button()),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                        ),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )