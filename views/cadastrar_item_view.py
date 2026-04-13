import flet as ft
import tkinter as tk
from tkinter import filedialog
from ui.theme import *
from controllers.cadastrar_item_controller import CadastrarItemController

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
        self.controller = CadastrarItemController()
        self._imagem_path = None

        # ===== INPUTS =====
        self.nome = Input(hint_text="Ex: Rothmans Blue Maço")
        self.valor = Input(hint_text="R$ 0,00")
        self.categoria = DropdownField([
            "Bebida", "Nacional", "Paraguai",
            "Comida", "Material", "Outros"
        ])

        # ===== PREVIEW =====
        self._preview_icon = ft.Icon(ft.Icons.IMAGE, color=TEXT_MUTED)

        self._preview_img = ft.Image(
            src="",
            visible=False,
            width=124,
            height=124,
            fit="cover",
        )

        self._preview_container = ft.Container(
            width=124,
            height=124,
            border_radius=16,
            bgcolor=BG_CARD_HOVER,
            alignment=ft.Alignment(0, 0),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Stack(
                controls=[
                    ft.Container(
                        width=124,
                        height=124,
                        alignment=ft.Alignment(0, 0),
                        content=self._preview_icon,
                    ),
                    self._preview_img,
                ]
            ),
        )

    # ===== ABRIR SELETOR DE ARQUIVO =====
    def _pick_file(self, e):
        # Janela tkinter invisível só para hospedar o filedialog
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)

        path = filedialog.askopenfilename(
            title="Selecionar imagem",
            filetypes=[("Imagens", "*.png *.jpg *.jpeg *.webp")]
        )

        root.destroy()

        if not path:
            return

        self._imagem_path = path
        self._preview_img.src = path
        self._preview_img.visible = True
        self._preview_icon.visible = False
        self.app.page.update()

    # ===== SALVAR =====
    def _save_item(self, e):
        nome = self.nome.value
        valor = self.valor.value.replace("R$", "").replace(",", ".").strip()
        categoria = self.categoria.value

        valido, msg = self.controller.validar(nome, valor, categoria)
        if not valido:
            print(msg)
            return

        imagem_salva = (
            self.controller.copiar_imagem(self._imagem_path)
            if self._imagem_path
            else "assets/images/default.png"
        )

        self.controller.salvar_item(
            nome=nome,
            valor=valor,
            categoria=categoria,
            imagem=imagem_salva,
        )

        print("Item cadastrado com sucesso!")
        self._reset()

        # Recarrega a ItensView antes de navegar
        itens_view = self.app.views.get("ItensView")
        if itens_view:
            itens_view.itens = itens_view.controller.carregar_itens() if hasattr(itens_view, 'controller') else [] 

    # ===== RESET =====
    def _reset(self):
        self.nome.value = ""
        self.valor.value = ""
        self.categoria.value = None
        self._imagem_path = None
        self._preview_img.src = ""
        self._preview_img.visible = False
        self._preview_icon.visible = True
        self.app.page.update()

    # ===== UI =====
    def render(self):
        return ft.Container(
            expand=True,
            bgcolor=BG_MAIN,
            alignment=ft.Alignment(0, 0),
            content=ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=24,
                controls=[
                    ft.Container(
                        alignment=ft.Alignment(0, 0),
                        padding=ft.padding.symmetric(horizontal=16),
                        content=ft.Column(
                            width=350,
                            spacing=24,
                            controls=[

                                # HEADER
                                ft.Row(
                                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.Icons.ARROW_BACK,
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

                                # CARD
                                ft.Container(
                                    alignment=ft.Alignment(0, 0),
                                    content=ft.Container(
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
                                                        self._preview_container,
                                                        ft.ElevatedButton(
                                                            height=124,
                                                            width=165,
                                                            bgcolor=BG_CARD_HOVER,
                                                            style=ft.ButtonStyle(
                                                                shape=ft.RoundedRectangleBorder(radius=16),
                                                            ),
                                                            on_click=self._pick_file,
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
                                                self.nome,

                                                ft.Row(
                                                    spacing=12,
                                                    controls=[
                                                        ft.Column(
                                                            spacing=6,
                                                            width=140,
                                                            controls=[
                                                                Label("Valor *"),
                                                                self.valor,
                                                            ],
                                                        ),
                                                        ft.Column(
                                                            expand=True,
                                                            spacing=6,
                                                            controls=[
                                                                Label("Categoria *"),
                                                                self.categoria,
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
                                                    on_click=self._save_item,
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