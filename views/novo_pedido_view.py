import flet as ft
from ui.theme import *
from services.item_service import carregar_itens
from ui.tag_colors import get_tag_color
from controllers.novo_pedido_controller import NovoPedidoController
from views.resumo_pedido_dialog import ResumoPedidoDialog


class NovoPedidoView:
    def __init__(self, app):
        self.app = app
        self.itens = carregar_itens()
        self.controller = NovoPedidoController(self.itens)

        self.root_stack = ft.Stack(expand=True)

        self.total_text = ft.Text("R$ 0.00", size=18, weight=ft.FontWeight.BOLD)

        self.resumo_button = ft.ElevatedButton(
            content=ft.Text("Resumo do Pedido"),
            height=44,
            disabled=True,
            on_click=self.abrir_resumo,
            style=ft.ButtonStyle(
                bgcolor={
                    ft.ControlState.DEFAULT: PRIMARY,
                    ft.ControlState.HOVERED: PRIMARY_HOVER,
                },
                shape=ft.RoundedRectangleBorder(radius=20),
            ),
        )

    # ================= MODAL =================
    def abrir_resumo(self, e):
        # evita abrir dois modais
        if len(self.root_stack.controls) > 1:
            return

        dialog = ResumoPedidoDialog(
            controller=self.controller,
            on_finalizar=self.finalizar_pedido,
            on_close=self.fechar_resumo,
        )
        dialog.rebuild()

        self.root_stack.controls.append(dialog)
        self.root_stack.update()

    def fechar_resumo(self):
        if len(self.root_stack.controls) > 1:
            self.root_stack.controls.pop()
            self.root_stack.update()

    def finalizar_pedido(self):
        print("Pedido finalizado:", self.controller.get_resumo())
        self.controller.limpar()
        self.app.show_view("PedidosView")

    # ================= ITEM CARD =================
    def item_selector_card(self, item):
        item_id = item["id"]
        valor = item["valor"] - item.get("desconto", 0)
        tag_color = get_tag_color(item.get("categoria"), PRIMARY)

        qtd_text = ft.Text("0", size=14, weight=ft.FontWeight.BOLD)

        card = ft.Container(
            width=360,
            padding=14,
            border_radius=18,
            bgcolor=BG_CARD,
            border=ft.border.all(1, BG_CARD),
        )

        def atualizar_ui():
            qtd = self.controller.get_qtd(item_id)
            qtd_text.value = str(qtd)
            card.border = ft.border.all(
                1, PRIMARY if qtd > 0 else BG_CARD
            )

            total = self.controller.calcular_total()
            self.total_text.value = f"R$ {total:.2f}"
            self.resumo_button.disabled = total == 0

            self.root_stack.update()

        def add(_):
            self.controller.add_item(item_id)
            atualizar_ui()

        def remove(_):
            self.controller.remove_item(item_id)
            atualizar_ui()

        card.content = ft.Row(
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
                        ft.Text(
                            item["nome"],
                            weight=ft.FontWeight.BOLD,
                            size=14,
                        ),
                        ft.Text(
                            f"R$ {valor:.2f}",
                            size=13,
                            color=TEXT_MUTED,
                        ),
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
                            on_click=remove,
                        ),
                        qtd_text,
                        ft.IconButton(
                            icon=ft.Icons.ADD,
                            icon_color=ft.Colors.BLUE_400,
                            on_click=add,
                        ),
                    ],
                ),
            ],
        )

        return card

    # ================= VIEW =================
    def render(self):
        main_view = ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            content=ft.Column(
                expand=True,
                controls=[
                    # HEADER
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

                    # BUSCA
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

                    # TÍTULO
                    ft.Container(
                        padding=ft.padding.only(20, 16, 20, 8),
                        content=ft.Text(
                            "SELECIONE OS ITENS",
                            size=12,
                            weight=ft.FontWeight.BOLD,
                            color=TEXT_MUTED,
                        ),
                    ),

                    # LISTA
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

                    # FOOTER
                    ft.Container(
                        margin=ft.margin.all(16),
                        padding=20,
                        bgcolor=BG_CARD,
                        border_radius=28,
                        content=ft.Row(
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            controls=[
                                self.total_text,
                                self.resumo_button,
                            ],
                        ),
                    ),
                ],
            ),
        )

        self.root_stack.controls = [main_view]
        return self.root_stack
