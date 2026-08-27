import flet as ft
from src.common.constants import PROJECT_TITLE
from src.databases.data_access import DAH, Item
from src.ui.items import Items as ItemsUI
from src.ui.settings import Settings as SettingsUI
from src.ui.create import CreateItemUI
from src.ui.body import Body
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
    def window2readitem():
        main_container.content = IUI.get()
        page.update()
    def window2createitem():
        main_container.content = CIUI.get()
        page.update()
    IUI = ItemsUI(page, window2createitem)
    CIUI = CreateItemUI(window2readitem)
    SUI = SettingsUI()
    BUI = Body()
    
    def on_nav_change(e):
        index = e.control.selected_index
        if index == 0:
            main_container.content = BUI.get()
        elif index == 1:
            window2readitem()
        elif index == 2:
            main_container.content = SUI.get()
        page.update()  # UI aktualisieren
    main_container = ft.Container(
        content=BUI.get(),
        expand=True,
        bgcolor=ft.Colors.BLUE_900,
        border_radius=ft.BorderRadius.all(5),
    )
    page.add(main_container)
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.FACE, label="Körper"),
            ft.NavigationBarDestination(icon=ft.Icons.FASTFOOD_SHARP, label="Ernährung"),
            ft.NavigationBarDestination(icon=ft.Icons.SETTINGS, label="Einstellungen"),
        ],
        on_change=lambda e: on_nav_change(e) # e.control.selected_index
    )

ft.run(main)