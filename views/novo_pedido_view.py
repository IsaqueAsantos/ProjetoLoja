import flet as ft
from ui.theme import *
from services.item_service import carregar_itens
from ui.tag_colors import get_tag_color

class NovoPedidoView:
    def __init__(self, app):
        self.app = app
        self.itens = carregar_itens()
        self.carrinho = {}
        self.total_text = ft.Text("R$ 0.00", size=18, weight=ft.FontWeight.BOLD)

    # ================= ITEM CARD =================
    def item_selector_card(self, item):
        item_id = item["id"]
        qtd_text = ft.Text(
        str(self.carrinho.get(item_id, 0)),
        size=14,
        )
        valor = item["valor"] - item.get("desconto", 0)

        tag_color = get_tag_color(item.get("categoria"), PRIMARY)

        def atualizar_total():
            total = 0
            for i in self.itens:
                q = self.carrinho.get(i["id"], 0)
                if q:
                    total += (i["valor"] - i.get("desconto", 0)) * q
            self.total_text.value = f"R$ {total:.2f}"
            self.app.page.update()

        #Contador de item
        def add(_):
            self.carrinho[item_id] = self.carrinho.get(item_id, 0) + 1
            qtd_text.value = str(self.carrinho[item_id])
            atualizar_total()
            qtd_text.update()

        #Remover do contador
        def remove(_):
            atual = self.carrinho.get(item_id, 0)

            if atual > 1:
                self.carrinho[item_id] = atual - 1
                qtd_text.value = str(self.carrinho[item_id])
            elif atual == 1:
                del self.carrinho[item_id]
                qtd_text.value = "0"

            atualizar_total()
            qtd_text.update()

        return ft.Container(
            width=360,
            padding=14,
            border_radius=18,
            bgcolor=BG_CARD,
            border=ft.border.all(1, PRIMARY if self.carrinho.get(item_id, 0) > 0 else BG_CARD),
            content=ft.Row(
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=56,
                        height=56,
                        border_radius=14,
                        clip_behavior=ft.ClipBehavior.ANTI_ALIAS,
                        content=ft.Image(
                            src=item.get("imagem", ""),
                            fit="cover",
                        ),
                    ),
                    ft.Container(width=12),
                    ft.Column(
                        expand=True,
                        spacing=4,
                        controls=[
                            ft.Text(item["nome"], weight=ft.FontWeight.BOLD, size=14),
                            ft.Text(f"R$ {valor:.2f}", size=13, color=TEXT_MUTED),
                            ft.Container(
                                padding=ft.padding.symmetric(4, 10),
                                bgcolor=tag_color,
                                border_radius=20,
                                content=ft.Text(
                                    item.get("categoria", ""),
                                    size=11,
                                    color=TEXT_PRIMARY,
                                ),
                            ),
                        ],
                    ),
                    ft.Row(
                        spacing=6,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.REMOVE,
                                icon_color=ft.Colors.RED_400,
                                bgcolor=BG_CARD,
                                on_click=remove,
                            ),

                            qtd_text,
                            ft.IconButton(
                                icon=ft.Icons.ADD,
                                icon_color=ft.Colors.BLUE_400,
                                bgcolor=BG_CARD,
                                on_click=add,
                            ),
                        ],
                    ),
                ],
            ),
        )

    # ================= VIEW =================
    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            content=ft.Column(
                expand=True,
                controls=[
                    # ===== HEADER =====
                    ft.Container(
                        padding=20,
                        content=ft.Row(
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
                                ft.Text("Novo Pedido", style=font_header()),
                            ],
                        ),
                    ),

                    # ===== BARRA DE BUSCA (FIXO) =====
                    ft.Container(
                        padding=20,
                        content=ft.Column(
                            controls=[
                                ft.Text("Filtro de Busca", style=font_label()),
                                ft.TextField(
                                    height=44,
                                    hint_text="Digite o nome do produto",
                                    bgcolor=BG_CARD,
                                    border_radius=14,
                                    border_color=BG_CARD,
                                    prefix_icon=ft.Icons.SEARCH,
                                ),
                            ],
                        ),
                    ),

                    # ===== TÍTULO FIXO =====
                    ft.Container(
                        padding=ft.padding.only(20, 16, 20, 8),
                        content=ft.Text(
                            "SELECIONE OS ITENS",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_MUTED,
                        ),
                    ),

                    # ===== LISTA COM SCROLL =====
                    ft.Container(
                        expand=True,
                        padding=20,
                        content=ft.Column(
                            scroll=ft.ScrollMode.AUTO,
                            controls=[
                                ft.Row(
                                    wrap=True,
                                    spacing=12,
                                    run_spacing=12,
                                    controls=[
                                        self.item_selector_card(item)
                                        for item in self.itens
                                    ],
                                ),
                                ft.Container(height=120),
                            ],
                        ),
                    ),

                    # ===== FOOTER FIXO =====
                    ft.Container(
                        margin=ft.margin.only(16, 16, 16, 16),
                        padding=20,
                        bgcolor=BG_CARD,
                        border_radius=28,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                self.total_text,
                                ft.ElevatedButton(
                                    content=ft.Text(
                                        "Finalizar Pedido",
                                        weight=ft.FontWeight.BOLD,
                                    ),
                                    height=44,
                                    style=ft.ButtonStyle(
                                        bgcolor={
                                            ft.ControlState.DEFAULT: PRIMARY,
                                            ft.ControlState.HOVERED: PRIMARY_HOVER,
                                        },
                                        shape=ft.RoundedRectangleBorder(radius=20),
                                    ),
                                ),
                            ],
                        ),
                    ),
                ],
            ),
        )
