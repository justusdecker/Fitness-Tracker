from src.ui.ui import UI
from src.databases.data_access import Item, DAH
from src.databases.items import NutrientSet
import flet as ft
class CreateItemUI(UI):
    def __init__(self, page_switch, items_ui):
        super().__init__()
        self.items_ui = items_ui
        self.page_switch = page_switch
        self.textfields: list[ft.TextField | ft.Button] = []
        

        for c in Item.__table__.columns:
            if c.name in NutrientSet.__dict__:
                print(f'is in {c.name}')
                
                other_objects = []
                
                for k in getattr(NutrientSet, c.name):
                    other_objects.append(ft.ListTile(ft.TextField(label= k.replace('_',' ').capitalize())))
                
                ETS = ft.Column(
                        spacing=0,
                        controls=[
                            ft.ExpansionTile(
                                expanded=True,
                                title=ft.Text(c.name.replace('_',' ').capitalize()),
                                subtitle=ft.Text("Placeholder"),
                                affinity=ft.TileAffinity.PLATFORM,
                                maintain_state=True,
                                collapsed_text_color=ft.Colors.BLACK,
                                text_color=ft.Colors.BLACK_87,
                                controls=other_objects
                            ),
                            
                        ],
                    )
                
                self.textfields.append(ETS)
            else:
                self.textfields.append(ft.TextField(label= c.name.replace('_',' ').capitalize()))

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
          
        