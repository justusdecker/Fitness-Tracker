import flet as ft

def getExpansionTileWColumn(text: str, objects, subtitle = 'Placeholder') -> ft.Column:
    return ft.Column(
            spacing=0,
            controls=[
                ft.ExpansionTile(
                    expanded=True,
                    title=ft.Text(text),
                    subtitle=ft.Text(subtitle),
                    affinity=ft.TileAffinity.PLATFORM,
                    maintain_state=True,
                    collapsed_text_color=ft.Colors.BLACK,
                    text_color=ft.Colors.BLACK_87,
                    controls=objects
                ),
                
            ],
        )