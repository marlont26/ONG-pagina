import flet as ft

def main(page: ft.Page):
    page.title = "Aplicación con Navbar - Flet"
    page.scroll = "always"
    page.bgcolor = "#343a40"  # Fondo de la página (gris oscuro)

    # Navbar con logo e íconos
    navbar = ft.Container(
        content=ft.Row(
            controls=[
                # Logo con enlace
                ft.TextButton(
                    content=ft.Row(
                        controls=[
                            ft.Image(
                                src="https://i.pinimg.com/originals/cb/83/63/cb8363735ab174defb79b1b6f164a5e2.jpg",
                                width=50,
                                height=50
                            ),
                            ft.Text("HappyPaws", size=20, color="black"),
                        ]
                    ),
                    on_click=lambda e: mostrar_pagina("Inicio", page),
                    style=ft.ButtonStyle(bgcolor="white")
                ),
                # Menú de navegación
                ft.TextButton(text="Home", on_click=lambda e: mostrar_pagina("Inicio", page), style=ft.ButtonStyle(color="black")),
                ft.TextButton(text="Adopciones", on_click=lambda e: mostrar_pagina("Adopciones", page), style=ft.ButtonStyle(color="black")),
                ft.TextButton(text="Sobre nosotros", on_click=lambda e: mostrar_pagina("Sobre Nosotros", page), style=ft.ButtonStyle(color="black")),
                ft.TextButton(text="Contáctanos", on_click=lambda e: mostrar_pagina("Contáctanos", page), style=ft.ButtonStyle(color="black")),
                ft.TextButton(text="Donaciones", on_click=lambda e: mostrar_pagina("Donaciones", page), style=ft.ButtonStyle(color="black")),
                # Botones de Login y Register
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.TextButton(text="Login", on_click=lambda e: mostrar_pagina("Login", page), style=ft.ButtonStyle(bgcolor="white", color="black")),
                            ft.TextButton(text="Register", on_click=lambda e: mostrar_pagina("Register", page), style=ft.ButtonStyle(bgcolor="blue", color="white")),
                        ]
                    ),
                    alignment=ft.alignment.center_right,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        padding=ft.padding.symmetric(vertical=15, horizontal=20),
        bgcolor="white",  # Fondo blanco para la navbar
    )

    # Contenedor para la página principal
    contenido_principal = ft.Container(
        content=ft.Text("Bienvenido a la aplicación. Selecciona una opción del menú.", color="white"),
        alignment=ft.alignment.center,
        padding=20,
        expand=True,
    )

    # Función para cambiar el contenido principal al hacer clic en un botón de la navbar
    def mostrar_pagina(nombre_pagina, page):
        contenido_principal.content = ft.Text(f"Estás en la página: {nombre_pagina}", color="white")
        page.update()

    # Agrega el navbar y el contenido principal a la página
    page.add(navbar, contenido_principal)

# Ejecuta la aplicación
ft.app(target=main)
