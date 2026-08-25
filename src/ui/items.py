from src.ui.ui import UI
import flet as ft
from src.backend.databases.data_access import DAH, Item
class Items(UI):
    def __init__(self):
        super().__init__()
        self.textfields = []
        for item in DAH.readItems():
            obj = ft.Container(
                ft.Column(
                    controls=[
                    ft.Text(item.title),
                    ft.Image(
                        src=item.img,
                        width=200,
                        height=150,
                        fit="cover",
                        border_radius=ft.BorderRadius.all(8),
                    ),
                    ft.ExpansionPanelList(
                        width=400,
                        controls=[
                            ft.ExpansionPanel(
                                header=ft.Text("Details"),
                                content=ft.Text(self.getNutritionInfo(item)),
                                
                            )
                        ],
                    )
                    ]
                ),
                bgcolor=ft.Colors.WHITE_10
            )
            self.textfields.append(obj)
        self.container = ft.Container(
            content=ft.ListView(
                    controls=self.textfields,
                    spacing=10,
                    padding=10,),
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )
    
    def getNutritionInfo(self,item):
        var_table = Item.getVarTableCropped()
        text = '\n'.join([f'{key:<15}{item.__getattribute__(key)}' for key in var_table])
        return text
    
    def enable(self): ...
    
    def get(self):
        return self.container