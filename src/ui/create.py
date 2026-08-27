from src.ui.ui import UI
from src.databases.items import Item
import flet as ft
class CreateItemUI(UI):
    def __init__(self, page_switch):
        super().__init__()
        self.textfields = []
        for key in Item.getVarTable():
            self.textfields.append(ft.TextField(label=key))
        
        self.textfields.append(
            ft.Button(content=ft.Text('Erstellen'), icon=ft.Icons.CREATE, on_click=page_switch)
            )
        
        
        list_container = ft.Container(
            content=ft.ListView(
                    controls=self.textfields,
                    spacing=10,
                    padding=10,),
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )
        self.container = ft.Column(
            controls=list_container
        )
    def get(self):
        return self.container
          
        