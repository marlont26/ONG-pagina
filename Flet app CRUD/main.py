import flet as ft
from pages.home import HomePage
from pages.add_item import AddItemPage
from pages.edit_item import EditItemPage
from pages.delete_item import DeleteItemPage

def main(page: ft.Page):
    page.title = "CRUD con Flet"
    # Tamaño inicial que simula una pantalla de celular
    page.window.width = 375  # Ancho típico de un dispositivo móvil (iPhone por ejemplo)
    page.window.height = 677  # Altura típica de un móvil

    # Hacer que la ventana sea adaptable (se puede redimensionar)
    #
    # page.window.resizable = True
    page.adaptive = True
    page.auto_scroll = True

    page.appbar = ft.AppBar(
        leading=ft.TextButton("New", style=ft.ButtonStyle(padding=0)),
        title=ft.Text("Adaptive AppBar"),
        actions=[
            ft.IconButton(ft.cupertino_icons.ADD, style=ft.ButtonStyle(padding=0))
        ],
        bgcolor=ft.colors.with_opacity(0.04, ft.cupertino_colors.SYSTEM_BACKGROUND),
    )

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.EXPLORE, label="Explore"),
            ft.NavigationBarDestination(icon=ft.icons.COMMUTE, label="Commute"),
            ft.NavigationBarDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Bookmark",
            ),
        ],
        border=ft.Border(
            top=ft.BorderSide(color=ft.cupertino_colors.SYSTEM_GREY2, width=0)
        ),
    )

    # Diccionario de rutas con las páginas
    routes = {
        "/": HomePage,
        "/add": AddItemPage,
        "/edit": EditItemPage,
        "/delete": DeleteItemPage,
    }

    # Función para manejar los cambios de ruta
    def route_change(route):
        page.controls.clear()  # Limpia los controles de la página actual
        current_page = routes.get(page.route, lambda p: HomePage(p))(page)
        page.add(current_page)  # Agrega la nueva página a los controles
        page.update()

    # Maneja los cambios de ruta
    page.on_route_change = route_change
    page.go(page.route)  # Navega a la ruta actual al iniciar

ft.app(target=main)
