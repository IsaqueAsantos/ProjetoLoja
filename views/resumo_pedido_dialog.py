import flet as ft
from ui.theme import *


class ResumoPedidoDialog(ft.Stack):
    def __init__(self, controller, on_finalizar, on_close):
        super().__init__(expand=True)

        self.controller = controller
        self.on_finalizar = on_finalizar
        self.on_close = on_close

        # ================= INPUTS =================
        self.cliente_input = ft.TextField(
            label="Nome do cliente",
            text_size=14,
            content_padding=ft.Padding(12, 14, 12, 14),
            expand=True,
        )

        self.desconto_input = ft.TextField(
            label="Desconto (%)",
            keyboard_type=ft.KeyboardType.NUMBER,
            prefix_icon=ft.Icons.PERCENT,
            text_size=14,
            content_padding=ft.Padding(12, 14, 12, 14),
            expand=True,
            on_change=self._on_desconto_change,
        )

        # ================= TEXTOS =================
        self.subtotal_text = ft.Text(size=13, color=TEXT_MUTED)
        self.desconto_valor_text = ft.Text(size=13, color=TEXT_MUTED)
        self.total_text = ft.Text(size=18, weight=ft.FontWeight.BOLD, color=PRIMARY)

        # ================= LISTA =================
        self.itens_list = ft.ListView(
            spacing=8,
            expand=True,
        )

        # ================= OVERLAY =================
        overlay = ft.Container(
            expand=True,
            bgcolor=ft.Colors.with_opacity(0.6, ft.Colors.BLACK),
            on_click=lambda e: self.fechar(),
        )

        # ================= MODAL =================
        modal = ft.Container(
            width=420,
            height=620,
            bgcolor=BG_CARD,
            border_radius=20,
            padding=20,
            content=ft.Column(
                spacing=14,
                controls=[
                    # HEADER
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Resumo do Pedido", size=20, weight=ft.FontWeight.BOLD),
                            ft.IconButton(
                                icon=ft.Icons.CLOSE,
                                icon_color=TEXT_MUTED,
                                on_click=lambda e: self.fechar(),
                            ),
                        ],
                    ),

                    # CLIENTE
                    self.cliente_input,

                    # ITENS
                    ft.Container(
                        height=220,
                        content=self.itens_list,
                    ),

                    ft.Divider(),

                    # SUBTOTAL
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Subtotal:", color=TEXT_MUTED),
                            self.subtotal_text,
                        ],
                    ),

                    # DESCONTO INPUT
                    self.desconto_input,

                    # DESCONTO APLICADO
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Desconto:", color=TEXT_MUTED),
                            self.desconto_valor_text,
                        ],
                    ),

                    # TOTAL
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Total Final:", size=16, weight=ft.FontWeight.BOLD),
                            self.total_text,
                        ],
                    ),

                    # BOTÃO À DIREITA
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.ElevatedButton(
                                content=ft.Text(
                                    "Finalizar Pedido",
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE,
                                ),
                                height=48,
                                width=200,
                                style=ft.ButtonStyle(
                                    bgcolor={ft.ControlState.DEFAULT: ft.Colors.GREEN},
                                    shape=ft.RoundedRectangleBorder(radius=16),
                                    elevation=0,
                                ),
                                on_click=self._finalizar,
                            ),
                        ],
                    ),
                ],
            ),
        )

        self.controls = [
            overlay,
            ft.Container(expand=True, alignment=ft.Alignment(0, 0), content=modal),
        ]

    # ======================================================
    def rebuild(self):
        self.itens_list.controls.clear()

        resumo = self.controller.get_resumo()
        subtotal = self.controller.calcular_subtotal()
        desconto_pct = self.controller.get_desconto()
        desconto_valor = subtotal * (desconto_pct / 100)
        total = self.controller.calcular_total()

        for item in resumo:
            preco_unit = item["subtotal"] / item["qtd"] if item["qtd"] else 0

            self.itens_list.controls.append(
                ft.Container(
                    padding=12,
                    border_radius=14,
                    bgcolor=ft.Colors.with_opacity(0.08, ft.Colors.WHITE),
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(item["nome"], weight=ft.FontWeight.BOLD),
                                    ft.Text(
                                        f"{item['qtd']}x R$ {preco_unit:.2f}",
                                        size=12,
                                        color=TEXT_MUTED,
                                    ),
                                ],
                            ),
                            ft.Text(
                                f"R$ {item['subtotal']:.2f}",
                                weight=ft.FontWeight.BOLD,
                            ),
                        ],
                    ),
                )
            )

        self.subtotal_text.value = f"R$ {subtotal:.2f}"
        self.desconto_valor_text.value = f"- R$ {desconto_valor:.2f}"
        self.total_text.value = f"R$ {total:.2f}"

    # ======================================================
    def _on_desconto_change(self, e):
        try:
            valor = float(self.desconto_input.value or 0)
        except ValueError:
            valor = 0

        self.controller.set_desconto(valor)
        self.rebuild()

        if self.page:
            self.page.update()

    def _finalizar(self, e):
        self.controller.set_cliente_nome(self.cliente_input.value)
        self.fechar()
        self.on_finalizar()

    def fechar(self):
        if self.page and self in self.page.controls:
            self.page.controls.remove(self)
            self.page.update()

        self.on_close()
