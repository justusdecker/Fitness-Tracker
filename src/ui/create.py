from src.ui.ui import UI
from src.databases.items import NutrientSet, ItemColumns, Item
import flet as ft
from src.ui.common.tf_creator import getExpansionTileWColumn
from src.common.decorators import notImplementedYet

def rusaac(text: str):
    """
    Replace underscore -> space, and apply capitalize
    """
    return text.replace('_',' ').capitalize()

def rsadc(text:str):
    """
    Converts rusaac strings back to database-compatible
    """
    return text.replace(' ','_').lower()

class CreateItemUI(UI):
    """
    Contains all of the needed functionality for building the UI for the *Creating* Sub-Page
    
    :param items_ui: the pointer to the `Item` Class. For resetting
    :param page_switch: The page the user will be redirected to. Usually `ItemUI`
    """
    def __init__(self, page_switch, items_ui):
        super().__init__()
        self.items_ui = items_ui
        self.page_switch = page_switch
        self.textfields: list[ft.TextField | ft.Button] = []
        
        essential_objects = []
        nutrition_table_objects = []
        _temp_textfields = []
        
        self.all_textfields = [] #? For fetching the data later
        
        for c in Item.__table__.columns:
            name: str = c.name
            rusaac_name = rusaac(name)
            
            if name in NutrientSet.__dict__:
                _temp_textfields.append(
                    self.createNutrientExpansionTileWColumn(name, rusaac_name)
                ) 
            elif name in ItemColumns.ESSENTIELL:
                obj = self.getLTATF(name, pre='ESSENTIELL')
                essential_objects.append(obj)
            elif name in ItemColumns.ERNÄHRUNGSTABELLE:
                obj = self.getLTATF(name, pre='ERNÄHRUNGSTABELLE')
                nutrition_table_objects.append(obj)
            elif name == 'id': continue #? Skip, we dont need it actually
            else:
                raise NotImplementedError(f'{rusaac_name} is not in ItemColumns or NutritionSet')


        ESSENTIALS = getExpansionTileWColumn(rusaac('ESSENTIELL'),essential_objects)
        
        NUTRITION_TABLE = getExpansionTileWColumn(rusaac('ERNÄHRUNGSTABELLE'), nutrition_table_objects)
        self.addTf(ESSENTIALS)
        self.addTf(NUTRITION_TABLE)
        self.textfields.extend(_temp_textfields)
        
        
        self.addTf(
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
        
    def addTf(self, obj):
        """
        Adds an Object to `self.textfields`
        
        :param obj: The object you want to add to the `self.textfields`
        """
        self.textfields.append(obj)
        
    def getTf(self, text: str, pre: str) -> ft.TextField:
        """
        Used for the Create System.
        
        Sets the ID inside `tf.TextField.innerData`
        
        
        :param pre: first part of the id
        :param text: second part of the id
        """
        tf = ft.TextField(label= rusaac(text))
        tf.innerData = { 'id': f'{pre}:{text}' }
        self.all_textfields.append(tf)
        return tf
    
    def getLTATF(self, text: str, pre: str) -> ft.ListTile:
        """
        
        Gets a `ft.ListTile` with the result of `self.getTf(text, pre)`
        
        :param pre: first part of the id
        :param text: second part of the id
        """
        return ft.ListTile(self.getTf(text, pre))
        
    def createNutrientExpansionTileWColumn(self, name: str, rname: str) -> ft.Column:
        """
        Creates and return the complete ExpansionTile for the NutritionEntry
        
        :param name: the key for fetching data of the `NutrientSet`
        :param rname: the modified `name` value, `rusaac(name)`
        
        """
        other_objects = []
        for k in getattr(NutrientSet, name):
            obj = self.getLTATF(k, name)
            other_objects.append(obj)
        
        ETS = getExpansionTileWColumn(rname, other_objects)
        return ETS
    @notImplementedYet
    def getAllEntrys(self) -> list:
        """
        
        """
        tree: dict[str, dict] = {}
        for entry in self.all_textfields:
            if 'id' not in entry.innerData:
                raise NotImplementedError()
            id = entry.innerData['id']
            _type, key = id.split(':')
            if _type in tree:
                tree[_type][key] = entry.value
            else:
                tree[_type] = {}

    
    def __orderTextFields(self) -> dict:
        """
        orders the textfields based on the `_type` and returns as a dict
        """
        ordered = {}
        for tf in self.all_textfields:
            _type, key = tf.innerData['id'].split(':')
            
            if _type == 'ESSENTIELL' or _type == 'ERNÄHRUNGSTABELLE':
                ordered[key] = tf.value if tf.value else None
                continue

            if _type in ordered:
                ordered[_type][key] = tf.value if tf.value else None
            else:
                ordered[_type] = {}
                ordered[_type][key] = tf.value if tf.value else None
        return ordered
    
    def createAndLeftPage(self):
        """
        sort the data, creates an item and switch/reset the page
        """
        data = self.__orderTextFields()
        Item.create(**data)
        self.items_ui.reset_list()
        self.page_switch()
    