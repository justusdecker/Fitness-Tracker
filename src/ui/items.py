from src.ui.ui import UI
import flet as ft
from src.backend.databases.data_access import DAH, Item
class Items(UI):
    def __init__(self, page):
        super().__init__()
        self.textfields = []
        
        for item in DAH.readItems():
            exp_btn = ft.Button(
                ft.Text(
                    item.title,
                    size=20, 
                    weight= ft.FontWeight.W_900),
                icon=ft.Icons.INFO, 
                on_click=lambda e: page.show_dialog(exp)) # ! Shows the wrong object because of the way lambda functions
            img = ft.Image(
                        src=item.img,
                        width=200,
                        height=150,
                        fit="cover",
                        border_radius=ft.BorderRadius.all(8),
                    )
            exp = ft.AlertDialog(
                title=ft.Text("Information"),
                content=ft.Text(self.getNutritionInfo(item)),
                actions=[ft.TextButton("Okay")],
                icon=ft.Icons.INFO
            )
            
            ammi = ft.TextField(label='Amount', width=120)
            enter = ft.Button(ft.Text('Enter'), width=120)
            obj = ft.Container(
                ft.Column(
                    controls=[
                    ft.Row(
                        controls=[
                            ft.Column(controls=[exp_btn, img]),
                            ft.Column(controls=[ammi, enter])],
                        ),
                    
                    ]
                ),
                bgcolor=ft.Colors.WHITE_10
            )
            self.textfields.append(obj)
        
        
        menu_and_search = ft.Row(
            controls=[
                ft.ContextMenu(
                    primary_items=[
                    ft.PopupMenuItem(content="Create", on_click=lambda e: print('click1')),
                    ft.PopupMenuItem(content="Update", on_click=lambda e: print('click2')),
                ],
                primary_trigger=ft.ContextMenuTrigger.DOWN,
                content=ft.Container(
                    key="context_menu_trigger_area",
                    expand=True,
                    bgcolor=ft.Colors.BLUE,
                    alignment=ft.Alignment.CENTER,
                    border_radius=ft.BorderRadius.all(12),
                    content=ft.Text("Menü"),
                )),
                
                ft.TextField(label = "Suche",
                             on_change=lambda e: print(e.control.value),

                            )
            ]
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
            controls=[
                menu_and_search,
                list_container
            ]
        )
    
    def getNutritionInfo(self,item):
        var_table = Item.getVarTableCropped()
        text = '\n'.join([f'{key:<15}{item.__getattribute__(key)}' for key in var_table])
        text += f'\n {item.title} {item.id}'
        return text
    
    def enable(self): ...
    
    def get(self):
        return self.container