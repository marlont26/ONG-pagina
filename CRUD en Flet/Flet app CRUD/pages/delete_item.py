import flet as ft
from models.crud import get_item1, delete_item, delete_user
from pages.home import preload_items, items
import asyncio

#items = asyncio.run(preload_items())

def DeleteItemPage(page):
    async def load_items():
        global items  # Asegúrate de que la variable global se esté usando
        items = await preload_items()  # Carga los ítems

    # Cargar ítems al inicio
    asyncio.run(load_items())  # Llama a la función asíncrona de carga de ítems
    
    def update_dropdown():
        asyncio.run(load_items()) 
        print(f"Actualizando dropdown")
        item_dropdown.options = [ft.dropdown.Option(text=item["name"], key=str(item["id"])) for item in items]
        item_dropdown.update()  # Actualizar el Dropdown
        page.update()  # Actualizar la página
        
    
        # Crear el Dropdown y cargar opciones
    item_dropdown = ft.Dropdown(
        label="Selecciona el item a eliminar",
        options=[ft.dropdown.Option(text=item["name"], key=str(item["id"])) for item in items],
    )

    def confirm_delete(e):
        if item_dropdown.value is not None:
            index = int(item_dropdown.value)
            print(item_dropdown.value+"---------------------") 
            print(f"Eliminando item con ID: {index}")
            asyncio.run(delete_user(index))
            update_dropdown()
            e.page.go("/")  # Regresa a la página principal

    return ft.Column([
        ft.Text("Eliminar Item"),
        item_dropdown,
        ft.ElevatedButton("Eliminar", on_click=confirm_delete),
        ft.ElevatedButton("Cancelar", on_click=lambda e: e.page.go("/")),
    ])