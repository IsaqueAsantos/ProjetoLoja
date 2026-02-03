import flet as ft
from ui.theme import *


def primary_button(
    text: str,
    on_click,
    icon: str | None = None,
    width: int = 320,
):
    return ft.Container(
        width=width,
        height=56,
        bgcolor=BG_CARD,
        border_radius=22,
        ink=True,
        on_click=on_click,
        content=ft.Row(
            spacing=12,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(icon, size=22, color=TEXT_PRIMARY)
                if icon
                else ft.Container(width=22),
                ft.Text(
                    text,
                    size=17,
                    weight=ft.FontWeight.BOLD,
                    color=TEXT_PRIMARY,
                ),
            ],
        ),
        padding=ft.padding.symmetric(horizontal=20),
        on_hover=lambda e: e.control.update(),
    )
