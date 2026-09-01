from src.ui.ui import UI
import flet as ft
from src.databases.data_access import DAH, Item
from src.databases.items import ItemColumns, NutrientSet
from datetime import datetime, timezone
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
                    bgcolor=ft.Colors.TRANSPARENT,
                    alignment=ft.Alignment.CENTER,
                    border_radius=ft.BorderRadius.all(12),
                    content=ft.IconButton(ft.Icons.MENU),
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
                content=self.getNutritionInfo(item),
                actions=[exp_t],
                icon=ft.Icons.INFO
            )
            exp_t.on_click = lambda e , exp = exp: close_dialog(e,exp)
            
            exp_btn = ft.Button(
                content=ft.Text(item.titel),
                icon=ft.Icons.INFO, 
                on_click=lambda e, exp = exp: self.page.show_dialog(exp)) # ! Shows the wrong object because of the way lambda functions
            
            amount_textfield = ft.TextField(label='Amount', width=120)
            amount_enter_button = ft.Button(ft.Text('Enter'), width=120)
            eatenlog_sumit_function = lambda e, amount_textfield = amount_textfield: self.createEntry(ammi)
            amount_textfield.on_submit = eatenlog_sumit_function
            amount_enter_button.on_click = eatenlog_sumit_function
            
            amount_textfield.innerData = {
                'item': item,
            }
            
            obj = ft.Container(
                ft.Column(
                    controls=[
                    ft.Row(
                        controls=[
                            ft.Column(controls=[exp_btn, img]),
                            ft.Column(controls=[amount_textfield, amount_enter_button])],
                        ),
                    
                    ]
                ),
                bgcolor=ft.Colors.WHITE_10
            )
            self.textfields.append(obj)
    
    def createEntry(self, amount_textfield):
        print('create')
        val = amount_textfield.value  
        data = {
            'amount': val,
            'timestamp': datetime.now(timezone.utc),
            'item': amount_textfield.innerData['item']
        }      
        DAH.createEatenLogEntry(**data)
        # * Get Time
        # * Check ammount
        # * reset -> eatenlog page
        
        
    def reset_list(self):
        # Alte Elemente entfernen
        self.list_view.controls.clear()
        print(self.list_view.controls.__len__())
        self.gen_new_textfields()
        # Neue Elemente hinzufügen
        print(self.textfields.__len__())
        
        
        # UI aktualisieren
        self.list_view.update()
    def getNutritionInfo(self, item) -> ft.DataTable:
        var_table = []

        # 1. Daten einsammeln
        unset_keys = 0
        unset_sub_keys = 0
        for col in Item.__table__.columns:
            key = col.name
            val = getattr(item, key, None)
            if val is None:
                unset_keys += 1
                if key in NutrientSet.__dict__:
                    for sub_key in getattr(NutrientSet, key):
                        unset_sub_keys += 1
                continue

            if key in NutrientSet.__dict__:
                for sub_key in getattr(NutrientSet, key):
                    sub_val = getattr(item, sub_key, None)
                    if sub_val is not None:
                        # Falls es sich um ein Gewicht/Mass-Objekt handelt, get() nutzen
                        formatted_val = sub_val.get('auto') if hasattr(sub_val, 'get') else str(sub_val)
                        var_table.append((sub_key, formatted_val))
                    else:
                        unset_sub_keys += 1
            elif key in ItemColumns.ESSENTIELL or key in ItemColumns.ERNÄHRUNGSTABELLE:
                
                formatted_val = val.get('auto') if hasattr(val, 'get') else str(val)
                if len(formatted_val) > 40:
                    formatted_val = formatted_val[:40] + '...' # Cap the string at 40 char max + 3 for ellipsies
                var_table.append((key, formatted_val))
        var_table.append(('Nicht gesetzt', str(unset_keys)))
        var_table.append(('Nicht gesetzt:s', str(unset_sub_keys)))
        # 2. Flet DataTable für das Popup generieren
        return ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nährstoff / Eigenschaft", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Wert", weight=ft.FontWeight.BOLD), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(k.replace('_', ' ').capitalize())),
                        ft.DataCell(ft.Text(str(v))),
                    ]
                )
                for k, v in var_table
            ],
            heading_row_height=40,
            data_row_min_height=35,
        )
    
    def enable(self): ...
    
    def get(self):
        return self.container