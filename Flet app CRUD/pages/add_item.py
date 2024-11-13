import flet as ft
from models.crud import add_item, create_user
from pages.ejbotones import main

def AddItemPage(page):
    item_name = ft.TextField(label="Nombre del Item")
    item_password = ft.TextField(label="Contraseña")
    
    async def save_item(e):
        await create_user(str(item_name.value), str(item_password.value))
        e.page.go("/")  # Regresar a la página principal
    
    content = ft.Column(
        [
            ft.Text("Agregar Nuevo Item"),
            item_name,
            item_password,
            ft.ElevatedButton("Guardar", on_click=save_item),
            ft.ElevatedButton("Cancelar", on_click=lambda e: e.page.go("/")),
        ],
        alignment=ft.MainAxisAlignment.START  # Alinear al inicio
    )
    
    # Botones en la parte inferior
    buttons = main(page) 

    # Retornar la página combinando ambas secciones
    return ft.Column(
        [
            content,  # El contenido se expande para ocupar el espacio
            buttons, # Alinear al centro en la parte inferior
        ],
            expand=True,  # Permite que la columna se expanda
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Alinear espacio entre contenido y botones
        )
    # return ft.Colum, n([
    #     ft.Text("Agregar Nuevo Item"),
    #     item_name,
    #     item_password,
    #     ft.ElevatedButton("Guardar", on_click=save_item),
    #     ft.ElevatedButton("Cancelar", on_click=lambda e: e.page.go("/")),
    #     main(page),
    # ])
