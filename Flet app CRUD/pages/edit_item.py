import flet as ft
from models.crud import update_user, preload_items
import asyncio

def EditItemPage(page):
    async def load_items():
        global items  # Asegúrate de que la variable global se esté usando
        items = await preload_items()  # Carga los ítems

    # Cargar ítems al inicio
    asyncio.run(load_items())  # Llama a la función asíncrona de carga de ítems
    # Campo para seleccionar el índice del item a editar
    item_dropdown = ft.Dropdown(
        label="Selecciona el item a editar",
        options=[ft.dropdown.Option(text=item["name"], key=str(item["id"])) for item in items],
    )

    # Campo para el nuevo valor del item
    new_item_name = ft.TextField(label="Nuevo nombre del Item")
    new_item_password = ft.TextField(label="Nueva contraseña del Item")
    
    # Función que se ejecuta cuando cambia el valor del Dropdown
    def item_selected(e):
        print("on_item_selected --------------")
        selected_item_id = int(item_dropdown.value)
        selected_item = next((item for item in items if item["id"] == selected_item_id), None)

        if selected_item:
            new_item_name.value = selected_item["name"]
            print(f"password --------- {selected_item.get("pass", "") }")
            new_item_password.value = selected_item.get("pass", "")  # Si el ítem tiene contraseña, la mostramos
            new_item_name.update()
            new_item_password.update()
        e.page.update()

    # Asignar el manejador de cambio de selección del Dropdown
    item_dropdown.on_change = item_selected
    
    def save_changes(e):
        if item_dropdown.value is not None and new_item_name.value:
            index = int(item_dropdown.value)
            asyncio.run(update_user(index, str(new_item_name.value), str(new_item_password.value)))
            e.page.go("/")  # Regresa a la página principal

    return ft.Column([
        ft.Text("Editar Item"),
        item_dropdown,
        new_item_name,
        new_item_password,
        ft.ElevatedButton("Guardar Cambios", on_click=save_changes),
        ft.ElevatedButton("Cancelar", on_click=lambda e: e.page.go("/")),
    ])
