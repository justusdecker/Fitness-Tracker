from src.ui.ui import UI
import flet as ft
import flet_charts as fch
from src.databases.body import EatenLog
from src.databases.items import Item, NutrientSet, ItemColumns
from src.common.unit_convert import Mass
from src.ui.common.tf_creator import getExpansionTileWColumn
from datetime import datetime, timezone
from src.common.text_edit import rusaac, rsadc

class BodyUI(UI):
    """
    Contains all of the needed functionality for building the UI for the *Body* Page
    """
    def __init__(self, page):
        super().__init__()
        self.page = page
        self.textfields = []
        avatar = ft.CircleAvatar(foreground_image_src='https://avatars.githubusercontent.com/u/200506279?v=4',width=120, height=120)
        
        name = ft.Text('Your Name Here')
        avatar_name = ft.Row(controls=[avatar, name])
        
        all_charts = [
            getExpansionTileWColumn(str(i), [self.getLC()], ) for i in range(10)
        ]
        lv = ft.ListView(

            controls=[
                      avatar_name,
                      *all_charts]
        )
        
        self.el = ft.ListView(
            controls=[]
        )
        
        self.refreshEatenLogNutritionInfo()
        
        bm = ft.ListView(
            controls=[
                ft.Text(f'bm_{i}') for i in range(12)
            ]
        )
        
        a = ft.ListView(
            controls=[
                ft.Text(f'a_{i}') for i in range(12)
            ]
        )
        
        result = self.getTabs(lv, self.el, bm, a)
        
        self.container = ft.Container(
            content=result,
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )
        
    def refreshEatenLogNutritionInfo(self, start = None):
        """
        Alle Daten müssen mit dem zugenommen faktor multipliziert werden
        
        Wichtige Daten:
        * Kalorien
        * Menge
        * mehr erst beim öffnen vom Tile
        """

        self.el.controls.clear()
        all_objects = []
        picker = ft.DatePicker()
        
        picker_btn = ft.Button(
            "Pick date",
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda _: self.page.show_dialog(picker),
        )
        
        # 1. Datum aus Picker bereinigen (Zeitzonen entfernen, Tag isolieren)
        if start is not None:
            # Nimm exakt das ausgewählte Kalenderdatum ohne UTC-Offset
            d = start.date()
            start = datetime(d.year, d.month, d.day, 0, 0, 0)
            end = datetime(d.year, d.month, d.day, 23, 59, 59, 999999)
            
        else: start, end = None, None
        
        
        def on_date_change(e):
            if picker.value:
                # Reiche das reine Datum weiter
                self.refreshEatenLogNutritionInfo(start=picker.value.astimezone().replace(tzinfo=None))
                self.el.update()

        picker.on_change = on_date_change
        
        all_objects.append(picker_btn)
        eaten_summary = {}
        for eaten_log in EatenLog.readDateRange(start, end): # TODO: Add Date Input
            eaten_log: EatenLog
            
            item: Item = eaten_log.item
            if item.serviermenge is None or item.serviermenge == '':
                serving_amount = Mass('100g')
            else:
                serving_amount = Mass(item.serviermenge)
 
            if eaten_log.amount is None or eaten_log.amount == '':
                amount = Mass('200g')
            else:    
                amount = Mass(eaten_log.amount)
            
            
            factor = amount / serving_amount
            generated_factor = factor.asFactor() # We need this to calculate the nutrients
            
            objects = []
            
            def deleteEatenLog(e, el = eaten_log):

                EatenLog.delete(el)
                self.refreshEatenLogNutritionInfo()
            
            delete_button = ft.FilledIconButton(ft.Icons.DELETE, on_click=deleteEatenLog)
            if item.vorschaubild:
                img = ft.Image(
                        src=item.vorschaubild if item.vorschaubild else "",
                        width=200,
                        height=150,
                        fit="cover",
                        border_radius=ft.BorderRadius.all(8),
                    )
                           
            cell_l = ft.DataCell(ft.Text(f'Menge'))
            cr_row = ft.Row(
                [
                ft.Text(f'{amount}'),
                ft.Text(f'({serving_amount})', weight=ft.FontWeight.BOLD, italic=True, color=ft.Colors.RED_800),
                ft.Text(f'({generated_factor})', weight=ft.FontWeight.BOLD, italic=True, color=ft.Colors.DEEP_PURPLE)
            ]
            )
            cell_r = ft.DataCell(cr_row)
            objects.append((cell_l, cell_r))
            
            for c in Item.__table__.columns:
                if c.name in NutrientSet.SETNAMES:
                    for s in getattr(NutrientSet, c.name):
                        ns = getattr(item, c.name)
                        if ns is None: continue
                        if s not in ns: continue
                        if ns[s] is None: continue
                        mass = Mass(ns[s])
                        
                        cell_l = ft.DataCell(ft.Text(f'{rusaac(c.name)} - {s}'))
                        cr_row = ft.Row(
                            [
                            ft.Text(f'{mass}'),
                            ft.Text(f'({mass * generated_factor})', weight=ft.FontWeight.BOLD, italic=True, color=ft.Colors.DEEP_PURPLE)
                        ]
                        )
                        cell_r = ft.DataCell(cr_row)
                        objects.append((cell_l, cell_r))
                        
                        if s in eaten_summary:
                            eaten_summary[s] += Mass(ns[s]) * generated_factor
                        else:
                            eaten_summary[s] = Mass(ns[s]) * generated_factor
                        
                        
                elif c.name in ItemColumns.ERNÄHRUNGSTABELLE:
                    val = getattr(item, c.name)
                    if val is None or val == '':
                        ...
                    else:
                        mass = Mass(val)    
                        cell_l = ft.DataCell(ft.Text(rusaac(c.name)))
                        cr_row = ft.Row(
                            [
                            ft.Text(f'{mass}'),
                            ft.Text(f'({mass * generated_factor})', weight=ft.FontWeight.BOLD, italic=True, color=ft.Colors.DEEP_PURPLE)
                        ]
                        )
                        cell_r = ft.DataCell(cr_row)
                        objects.append((cell_l, cell_r))
                        if c.name in eaten_summary:
                            eaten_summary[c.name] += Mass(val) * generated_factor
                        else:
                            eaten_summary[c.name] = Mass(val) * generated_factor
                        
                        
            DATATABLE = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Nährstoff / Eigenschaft", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Wert", weight=ft.FontWeight.BOLD), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        l,
                        r,
                    ]
                )
                for l, r in objects
            ],
            heading_row_height=40,
            data_row_min_height=35,
        )      
            
         
            
            timestamp = eaten_log.timestamp
            gETC_vars = [img, delete_button, DATATABLE] if item.vorschaubild else [delete_button, DATATABLE]
            obj = getExpansionTileWColumn(item.titel, gETC_vars, f'{timestamp}')
            key=f"eaten_log_entry_{eaten_log.id}"
            obj.key = key
            all_objects.append(
                obj
            )
        
        SUMMARY = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nährstoff / Eigenschaft", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Wert", weight=ft.FontWeight.BOLD), numeric=True),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(f'{k}')),
                    ft.DataCell(ft.Text(f'{eaten_summary[k]}')),
                ]
            )
            for k in eaten_summary
        ],
        heading_row_height=40,
        data_row_min_height=35,
    )   
        all_objects.insert(0, SUMMARY)
        all_objects.append(ft.Text('Keine weiteren Einträge gefunden'))
            
        print(len(all_objects))
        self.el.controls.extend(all_objects)
        try:
            self.el.update()
        except: ...
        self.page.update()

    def getTabs(self, lv, el, bm, a) -> ft.Tabs:
        """
        Returns the Tabs for the Body Page, contains e.g.: Analysis, Activity etc.
        """
        return ft.Tabs(
            length=4,
            expand=True,
            content=ft.Column(
                expand=True,
                controls=[
                    ft.TabBar(
                        tabs=[
                            ft.Tab(label="Analyse", icon= ft.Icons.ANALYTICS),
                            ft.Tab(label="Ernährung", icon=ft.Icons.FOOD_BANK),
                            ft.Tab(label="Körpermaße", icon=ft.Icons.BOY_ROUNDED),
                            ft.Tab(label="Aktivität", icon=ft.Icons.SPORTS)
                        ]
                    ),
                    ft.TabBarView(
                        expand=True,
                        controls=[
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=lv,
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=el,
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=bm,
                            ),
                            ft.Container(
                                alignment=ft.Alignment.CENTER,
                                content=a,
                            ),
                        ],
                    ),
                ],
            ),
        )
    
    def getLC(self) -> ft.Container:
        """
        Returns an Container filled with LineCharts for analysis.
        """
        return ft.Container(
            
            border_radius=ft.BorderRadius.all(12),
            
            bgcolor=ft.Colors.WHITE_12,
            content=
            
                ft.Column(
                    tight=True,
                controls=[
                    fch.LineChart(
                        width= 400,
                min_y=0,
                max_y=3,
                min_x=0,
                max_x=5,     
                data_series=[
                    fch.LineChartData(
                        color=ft.Colors.BLACK,
                           
                        curved=True,
                        points=[
                            fch.LineChartDataPoint(0, 1),
                            fch.LineChartDataPoint(1, 0.5),
                            fch.LineChartDataPoint(2, 1.5),
                            fch.LineChartDataPoint(3, 1),
                            fch.LineChartDataPoint(4, 0.5),
                            fch.LineChartDataPoint(5, 1.5),
                            
                        ],
                    ),]
                    )
                
                
                
                ],
            ))