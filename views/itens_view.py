import flet as ft
from ui.theme import *
from services.item_service import carregar_itens
from ui.tag_colors import get_tag_color

CARD_WIDTH = 190
CARD_HEIGHT = 300

class ItensView:
    def __init__(self, app):
        self.app = app
        self.itens = carregar_itens()

    def card_item(self, item):
        valor_final = item["valor"] - item.get("desconto", 0)
        categoria = item.get("categoria", "").lower()
        tag_color = get_tag_color(item.get("categoria"), PRIMARY)

        return ft.Container(
            width=CARD_WIDTH,
            height=CARD_HEIGHT,
            padding=14,
            bgcolor=BG_CARD,
            border_radius=18,
            content=ft.Column(
                spacing=10,
                controls=[
                    # ===== IMAGEM =====
                    ft.Container(
                        height=150,
                        border_radius=14,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Image(
                            src=item.get("imagem", ""),
                            fit="cover",
                        ),
                    ),

                    # ===== NOME + TAG =====
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                item["nome"],
                                style=font_text(),
                                weight=ft.FontWeight.BOLD,
                                max_lines=2,
                                overflow=ft.TextOverflow.ELLIPSIS,
                            ),
                            ft.Container(
                                padding=ft.padding.symmetric(6, 10),
                                bgcolor=tag_color,
                                border_radius=20,
                                content=ft.Text(
                                    item.get("categoria", ""),
                                    size=12,
                                    color=TEXT_PRIMARY,
                                ),
                            ),
                        ],
                    ),

                    # ===== ID =====
                    ft.Text(
                        f"ID: {item['id']}",
                        size=12,
                        color=TEXT_MUTED,
                    ),

                    ft.Container(height=6),

                    # ===== PREÇO + AÇÕES =====
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Container(
                                width=90,
                                content=ft.Text(
                                    f"R$ {valor_final:.2f}",
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                ),
                            ),
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.MODE_EDIT_OUTLINED,
                                        icon_color=ft.Colors.BLUE_400,
                                        padding=1,
                                        on_click=lambda e, i=item: print("Editar", i),
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE_OUTLINED,
                                        icon_color=ft.Colors.RED_400,
                                        padding=1,
                                        on_click=lambda e, i=item: print("Excluir", i),
                                    ),
                                ],
                            ),
                        ],
                    ),
                ],
            ),
        )
    
    def render(self):
        return ft.Container(
            expand=True,
            padding=20,
            bgcolor=BG_MAIN,
            content=ft.Column(
                scroll=ft.ScrollMode.AUTO,
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
                            ft.Text(
                                "Itens Cadastrados",
                                style=font_header(),
                            ),
                        ],
                    ),

                    ft.Container(height=16),

                    # ===== BUSCA =====
                    ft.TextField(
                        hint_text="Buscar itens...",
                        prefix_icon=ft.Icons.SEARCH_OUTLINED,
                        bgcolor=BG_CARD,
                        border_radius=20,
                        border_color=BG_CARD,
                    ),

                    ft.Container(height=20),

                    # ===== GRID FLEXÍVEL =====
                    ft.Row(
                        wrap=True,
                        spacing=20,
                        run_spacing=20,
                        controls=[self.card_item(item) for item in self.itens],
                    ),
                ],
            ),
        )