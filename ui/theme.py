import flet as ft

# =========================
# 🎨 CORES
# =========================

BG_MAIN = "#020617"
BG_CARD = "#1e293b"
BG_CARD_HOVER = "#334155"

PRIMARY = "#2563eb"
PRIMARY_HOVER = "#1d4ed8"

TEXT_PRIMARY = "#f8fafc"
TEXT_SECONDARY = "#e5e7eb"
TEXT_MUTED = "#94a3b8"


# =========================
# 🔤 FONTES (TextStyle)
# =========================

def font_title():
    return ft.TextStyle(
        size=26,
        weight=ft.FontWeight.BOLD,
        color=TEXT_PRIMARY,
    )


def font_header():
    return ft.TextStyle(
        size=20,
        weight=ft.FontWeight.BOLD,
        color=TEXT_PRIMARY,
    )


def font_button():
    return ft.TextStyle(
        size=17,
        weight=ft.FontWeight.BOLD,
        color=TEXT_PRIMARY,
    )


def font_text():
    return ft.TextStyle(
        size=14,
        color=TEXT_SECONDARY,
    )


def font_label():
    return ft.TextStyle(
        size=13,
        weight=ft.FontWeight.BOLD,
        color=TEXT_MUTED,
    )
