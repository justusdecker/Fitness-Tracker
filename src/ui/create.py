from src.ui.ui import UI
from src.databases.data_access import Item, DAH
import flet as ft
class CreateItemUI(UI):
    def __init__(self, page_switch, items_ui):
        super().__init__()
        self.items_ui = items_ui
        self.page_switch = page_switch
        self.textfields: list[ft.TextField | ft.Button] = []
        for key in Item.getVarTable():
            self.textfields.append(ft.TextField(label=key))
        
        self.textfields.append(
            ft.Button(content=ft.Text('Erstellen'), icon=ft.Icons.CREATE, on_click=self.createAndLeftPage)
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
    def createAndLeftPage(self):
        data = {tf.label: tf.value for tf in self.textfields if isinstance(tf, ft.TextField)}
        print(data)
        
        tk = Item.getVarTable()
        
        for key in tk:
            if key in data:
                if data[key] == '': 
                    data[key] = None
                    continue
        DAH.createItem(**data)
        self.items_ui.reset_list()
        self.page_switch()
    def get(self):
        return self.container
          
        