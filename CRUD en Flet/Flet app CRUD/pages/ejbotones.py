import flet as ft

def main(page: ft.Page):
    # Detectar si la pantalla es móvil o no
    is_mobile = page.window.width < 600  # Umbral típico para móvil

    # Crear los botones
    button1 = ft.ElevatedButton(text="Button 1")
    button2 = ft.ElevatedButton(text="Button 2")
    button3 = ft.ElevatedButton(text="Button 3")

    # Disposición para móvil (botones abajo)
    if is_mobile:
        buttons = ft.Row(
            [button1, button2, button3], 
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
        page.vertical_alignment = ft.MainAxisAlignment.END  # Alinear abajo en móvil
    
    # Disposición para web (botones en columna)
    else:
        buttons = ft.Column(
            [button1, button2, button3],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

    return buttons
