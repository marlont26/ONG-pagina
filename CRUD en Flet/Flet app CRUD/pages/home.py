import flet as ft
from models.crud import get_items, get_item1, preload_items, items
import asyncio

def HomePage(page):
    async def load_items():
        global items  # Asegúrate de que la variable global se esté usando
        items = await preload_items()  # Carga los ítems

    # Cargar ítems al inicio
    asyncio.run(load_items())  # Llama a la función asíncrona de carga de ítems
    
    # Crear la vista de la lista inicialmente vacía
    list_view = ft.ListView(
        expand=True,  # Permite que el ListView se expanda
    )

    # Función para obtener los ítems y actualizar la lista
    def go_to_getitems(e):
        print("Entrando a obtener items")
        asyncio.run(preload_items())
        list_view.controls.clear()  # Limpiar la lista actual
        for item in items:
            # Crear un ExpansionTile para cada ítem
            expansible = ft.ExpansionTile(
                title=ft.Text(f"ExpansionTile {item['id']}"),
                subtitle=ft.Text("Trailing expansion arrow icon"),
                affinity=ft.TileAffinity.PLATFORM,
                maintain_state=True,
                collapsed_text_color=ft.colors.RED,
                controls=[
                    ft.ListTile(title=ft.Text("This is sub-tile number 1"))
                ]
            )
            list_view.controls.append(expansible)  # Agregar el ExpansionTile a la lista

        page.update()  # Actualizar la página

    # Cargar los ítems al iniciar la página
    go_to_getitems(None)

    # Funciones para manejar la navegación
    def go_to_add(e):
        e.page.go("/add")
    
    def go_to_delete(e):
        e.page.go("/delete")

    def go_to_edit(e):
        e.page.go("/edit")
    # Retornar la interfaz de usuario
    content = ft.Column(
    [
        ft.Text("Lista de Items"),
        list_view, # Agregar la columna principal con el título y el ListView
        ft.ResponsiveRow([                
            ft.ElevatedButton("Agregar Item", on_click=go_to_add),
            ft.ElevatedButton("Eliminar", on_click=go_to_delete),
            ft.ElevatedButton("Editar", on_click=go_to_edit),
            ft.ElevatedButton("Actualizar items", on_click=go_to_getitems)
        ]),
    ],
        alignment=ft.MainAxisAlignment.START  # Alinear al inicio
    )
    
        # Crear un contenedor que soporte scroll
    scrollable_container = ft.Container(        
        content,
        height=500,  # Establecer una altura fija, ajusta según sea necesario
    )
    
    return ft.Column([scrollable_container],
        expand=True,  # Permite que la columna se expanda
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN  # Alinear espacio entre contenido y botones
    )


  