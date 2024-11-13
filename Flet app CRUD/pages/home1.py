import flet as ft
from models.crud import get_items1  # Asegúrate de que get_items esté obteniendo los datos del servidor Flask
import asyncio

def HomePage():
    async def update_item_list(e):
        """Actualizar la lista de elementos después de cualquier operación."""
        items = get_items1()

        list_view.controls.clear()  # Limpiar la lista actual
        for item in items:
            # Crear una tarjeta (ecard) por cada ítem
            card = ft.Card(
                content=ft.Column(
                    controls=[
                        ft.Text(f"Elemento: {item['nombre']}"),
                        ft.Text(f"Descripción: {item['descripcion']}"),
                        ft.Text(f"Fecha: {item['fecha']}")
                    ]
                )
            )
            list_view.controls.append(card)
        e.page.update()

    list_view = ft.ListView()

    async def handle_update_click(e):
        """Manejar el clic del botón para actualizar la lista."""
        await update_item_list()

    def go_to_add(e):
        """Navegar a la página de agregar ítem."""
        e.page.go("/add")

    def go_to_delete(e):
        """Navegar a la página de eliminar ítem."""
        e.page.go("/delete")

        # Cargar los ítems inicialmente
    asyncio.run(update_item_list())
    # Botón para actualizar la lista manualmente
    update_button = ft.ElevatedButton(
        "Actualizar lista", 
        on_click=lambda _: asyncio.create_task(handle_update_click(_))  # Llamar de manera asíncrona
    )

    return ft.Column([
        ft.Text("Lista de Items"),
        list_view,
        ft.ElevatedButton("Agregar Item", on_click=go_to_add),
        ft.ElevatedButton("Eliminar", on_click=go_to_delete),
        update_button,
    ], expand=True)
