from src.ui.ui import UI
import flet as ft
class Settings(UI):
    """
    !NotImplementedYet
    """
    def __init__(self):
        super().__init__()
        self.textfields = []
        self.container = ft.Container(
            content=ft.Placeholder(),
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )