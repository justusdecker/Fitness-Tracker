from src.ui.ui import UI
import flet as ft
import flet_charts as fch

from src.ui.common.tf_creator import getExpansionTileWColumn
class BodyUI(UI):
    def __init__(self):
        super().__init__()
        self.textfields = []
        avatar = ft.CircleAvatar(foreground_image_src='https://avatars.githubusercontent.com/u/200506279?v=4',width=120, height=120)
        name = ft.Text('Your Name Here')
        avatar_name = ft.Row(controls=[avatar, name])
        
        all_charts = [
            getExpansionTileWColumn(str(i), [self.getLC()], ) for i in range(10)
        ]
        
        result = ft.ListView(

            controls=[avatar_name,
                      *all_charts]
        )
        
        self.container = ft.Container(
            content=result,
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )
        
    def getLC(self):
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
            
        
    
    def get(self):
        return self.container