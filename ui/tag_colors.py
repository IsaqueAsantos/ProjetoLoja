import flet as ft

TAG_COLORS = {
    "cigarro": ft.Colors.RED_400,
    "bebida": ft.Colors.BLUE_400,
    "comida": ft.Colors.ORANGE_400,
    "material": ft.Colors.GREEN_400,
    "outros": ft.Colors.GREY_700,
}

def get_tag_color(categoria: str, default):
    if not categoria:
        return default

    key = categoria.strip().lower()
    return TAG_COLORS.get(key, default)
