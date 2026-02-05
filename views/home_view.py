import flet as ft
import asyncio
from ui.theme import *


class HomeView:
    def __init__(self, app):
        self.app = app
        self.menu_open = False

        self.menu_items_data = [
            ("Pedidos", ft.Icons.RECEIPT_LONG, "PedidosView"),
            ("Itens Cadastrados", ft.Icons.INVENTORY_2_OUTLINED, "ItensView"),
            ("Cadastrar", ft.Icons.ADD_CIRCLE_OUTLINE, "CadastrarView"),
            ("Histórico", ft.Icons.HISTORY, "HistoricoView"),
            ("Verificar Atualizações", ft.CupertinoIcons.ARROW_2_CIRCLEPATH, "AtualizacoesView"),
        ]

        self.menu_controls = []

        # ================= OVERLAY =================
        self.overlay = ft.Container(
            expand=True,
            bgcolor=ft.Colors.BLACK_12,
            opacity=0,
            visible=False,
            animate_opacity=300,
            on_click=lambda e: asyncio.create_task(self.close_menu()),
        )

        # ================= DRAWER =================
        self.drawer = ft.Container(
            width=350,
            expand=True,
            left=-350,
            animate_position=350,
            padding=20,
            bgcolor="#0E1625",
            content=self.drawer_content(),
        )

    # ================= MENU OPEN / TOGGLE =================
    async def toggle_menu(self, e=None):
        if self.menu_open:
            await self.close_menu()
            return

        self.menu_open = True

        self.overlay.visible = True
        self.drawer.left = 0
        self.overlay.opacity = 0.5

        self.reset_menu_items()

        self.drawer.update()
        self.overlay.update()

        await asyncio.sleep(0.01)  # frame de respiro
        await self.animate_menu_items()

    # ================= MENU CLOSE =================
    async def close_menu(self):
        if not self.menu_open:
            return

        self.menu_open = False

        self.drawer.left = -350
        self.overlay.opacity = 0

        self.drawer.update()
        self.overlay.update()

        await asyncio.sleep(0.3)  # tempo da animação

        self.overlay.visible = False
        self.overlay.update()

        self.reset_menu_items()

    # ================= MENU ITEM =================
    def menu_item(self, text, icon, route):
        return ft.Container(
            height=88,
            margin=ft.margin.only(bottom=8),
            padding=ft.padding.symmetric(horizontal=18),
            border_radius=16,
            bgcolor=BG_CARD,
            ink=True,
            opacity=0,
            offset=ft.Offset(-0.8, 0),
            animate_offset=800,
            animate_opacity=800,
            on_click=lambda e: self.app.show_view(route) if route else None,
            content=ft.Row(
                spacing=14,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Container(
                        width=44,
                        height=44,
                        border_radius=12,
                        bgcolor=PRIMARY,
                        alignment=ft.Alignment(0, 0),
                        content=ft.Icon(icon, color=ft.Colors.WHITE, size=22),
                    ),
                    ft.Text(
                        text,
                        size=17,
                        weight=ft.FontWeight.BOLD,
                        color=TEXT_PRIMARY,
                        expand=True,
                    ),
                    ft.Icon(
                        ft.Icons.CHEVRON_RIGHT,
                        color=TEXT_MUTED,
                        size=22,
                    ),
                ],
            ),
        )

    # ================= DRAWER CONTENT =================
    def drawer_content(self):
        self.menu_controls = [
            self.menu_item(text, icon, route)
            for text, icon, route in self.menu_items_data
        ]

        return ft.Column(
            spacing=14,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Column(
                            spacing=4,
                            controls=[
                                ft.Text("Menu", style=font_header()),
                                ft.Text(
                                    "Sistema de Pedidos",
                                    size=16,
                                    color=TEXT_MUTED,
                                ),
                            ],
                        ),
                        ft.IconButton(
                            icon=ft.Icons.CLOSE,
                            icon_color=TEXT_PRIMARY,
                            bgcolor=BG_CARD,
                            on_click=lambda e: asyncio.create_task(self.close_menu()),
                        ),
                    ],
                ),
                ft.Container(height=6),
                *self.menu_controls,
            ],
        )

    # ================= ANIMAÇÕES =================
    async def animate_menu_items(self):
        for item in self.menu_controls:
            item.opacity = 1
            item.offset = ft.Offset(0, 0)
            item.update()
            await asyncio.sleep(0.05)

    def reset_menu_items(self):
        for item in self.menu_controls:
            item.opacity = 0
            item.offset = ft.Offset(-0.8, 0)
            item.update()

    # ================= VIEW =================
    def render(self):
        return ft.Stack(
            expand=True,
            controls=[
                ft.Container(expand=True, bgcolor=BG_MAIN),

                ft.Container(
                    top=16,
                    left=16,
                    content=ft.IconButton(
                        icon=ft.Icons.MENU,
                        icon_color=TEXT_PRIMARY,
                        bgcolor=BG_CARD,
                        on_click=lambda e: asyncio.create_task(self.toggle_menu()),
                    ),
                ),

                self.overlay,
                self.drawer,
            ],
        )