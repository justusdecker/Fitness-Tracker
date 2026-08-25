import flet as ft
from src.common.constants import PROJECT_TITLE

from src.backend.databases.data_access import DAH, Item
for i in range(5):
    DAH.createItem(
        **{
            'title': 'test_object' + str(i),
            'img': 'https://www.vitaminexpress.org/_next/image?url=https%3A%2F%2Fimages.cdn.europe-west1.gcp.commercetools.com%2F783def08-dd2b-475d-b671-c397c0c2dbd7%2F6958-04-L-Arginin_70-SjmjxvAb.png&w=1440&q=80'
        }
    )
    
def main(page: ft.Page):
    page.title = PROJECT_TITLE
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    textfields = []
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
                )
                ]
            ),
            bgcolor=ft.Colors.WHITE_10
        )
        textfields.append(obj)
    
    
    page.add(
        ft.Container(
            content=ft.ListView(
                    controls=textfields,
                    spacing=10,
                    padding=10,),
            bgcolor=ft.Colors.BLUE_GREY_500,  
            border_radius=ft.BorderRadius.all(5),
            expand=True
        )
        )

ft.run(main)