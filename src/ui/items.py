from src.ui.ui import UI
import flet as ft
from src.databases.data_access import DAH, Item

class Items(UI):
    def __init__(self, page, page_switch):
        super().__init__()
        self.textfields = []
        
        self.page = page
        self.gen_new_textfields()
        
        menu_and_search = ft.Row(
            controls=[
                ft.ContextMenu(
                    primary_items=[
                    ft.PopupMenuItem(content="Create", on_click=page_switch),
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
                
                ft.TextField(label = "Suche", #! Switch to SearchBar
                             on_change=lambda e: print(e.control.value),

                            )
            ]
        )
        
        self.list_view = ft.ListView(
                    controls=self.textfields,
                    spacing=10,
                    padding=10,)
        
        list_container = ft.Container(
            content=self.list_view,
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
        
    def gen_new_textfields(self):
        self.textfields.clear()
        def close_dialog(e, dlg):
            
            dlg.open = False
            e.page.update()
        for item in DAH.readItems():
            item: Item
            
            
            img = ft.Image(
                        src=item.vorschaubild,
                        width=200,
                        height=150,
                        fit="cover",
                        border_radius=ft.BorderRadius.all(8),
                    )
            exp_t = ft.TextButton("Okay")
            exp = ft.AlertDialog(
                title=ft.Text("Information"),
                content=ft.Text(self.getNutritionInfo(item)),
                actions=[exp_t],
                icon=ft.Icons.INFO
            )
            exp_t.on_click = lambda e , exp = exp: close_dialog(e,exp)
            
            exp_btn = ft.Button(
                content=ft.Text(item.titel),
                icon=ft.Icons.INFO, 
                on_click=lambda e, exp = exp: self.page.show_dialog(exp)) # ! Shows the wrong object because of the way lambda functions
            
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
    def reset_list(self):
        # Alte Elemente entfernen
        self.list_view.controls.clear()
        print(self.list_view.controls.__len__())
        self.gen_new_textfields()
        # Neue Elemente hinzufügen
        print(self.textfields.__len__())
        
        
        # UI aktualisieren
        self.list_view.update()
    def getNutritionInfo(self,item):
        return ''
        var_table = Item.getVarTableCropped()
        text = '\n'.join([f'{key:<15}{item.__getattribute__(key)}' for key in var_table if item.__getattribute__(key) is not None])
        text += f'\n {item.title} {item.id}'
        return text
    
    def enable(self): ...
    
    def get(self):
        return self.container