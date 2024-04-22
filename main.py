import flet as ft


def main(page: ft.Page):
    page.bgcolor = ft.colors.BLACK
    page.tittle = "Hábitos App"
    page.padding = ft.padding.all(30)

    layout = ft.Column(
        expand = True,
        controls=[
            ft.Text(value="Que bom ter você aqui", size=30, color=ft.colors.WHITE),
            ft.Text(value="Como estão seus hábitos hoje?", size=20, color=ft.colors.GREY),

            ft.Container(
                padding = ft.padding.all(30),
                bgcolor = ft.colors.INDIGO,
                border_radius = ft.border_radius.all(20),
                margin= ft.margin.symmetric(vertical=30),
                content = ft.Column(
                    controls =[
                        ft.Text(value='Sua evolução hoje', size=20, color=ft.colors.WHITE),
                        progress_text := ft.Text(value='0%',  size=50, color=ft.colors.WHITE),
                        progress_bar := ft.ProgressBar(
                            value=0,
                            color=ft.colors.INDIGO_900,
                            bgcolor=ft.colors.INDIGO_100,
                            height=20,
                        ),
                    ],
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                ),
            ),
            ft.Text(value='Hábitos de hoje', size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
            ft.Text(value='Marcar suas tarefas como concluído te motiva a continuar focado', size=16, color=ft.colors.WHITE),

            habits := ft.Container(
                expand = True,
                padding = ft.padding.all(20),
                bgcolor = ft.colors.GREY_900,
                border_radius = ft.border_radius.all(20),
                margin = ft.margin.symmetric(vertical=20) 
                content = ft.Column(
                    expand = True,
                    scroll = ft.ScrollMode.AUTO,
                    spacing = 20
                    controls =[
                        ft.Checkbox()
                    ] 
                ),
            ),
        ] 
    )
    
    page.add(layout)

    page.update()


ft.app(main)
