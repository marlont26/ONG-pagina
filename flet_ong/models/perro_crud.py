import httpx
import requests

items = []  

async def preload_items():
    global items  # Indica que usaremos la variable global
    print("Preloading items --------------------------------")
    items = await get_item1()
    return items

async def get_item1():
    try:
        # Hacemos la solicitud al endpoint de Flask
        print("Entra a listar")
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:80/perrosgod/perrostt")
        print(f"Entra a listar 1 {response.status_code}")

        if response.status_code == 200:
            perros = response.json()
            print(f"Entra a listar {perros}")
            
            data = response.json()
            return [{"id": perro["id"], 
                    "nombre": perro["nombre"],
                    "raza": perro["raza"],
                    "edad": perro["edad"],
                    "estadoSalud": perro["estadoSalud"],
                    "descripcion": perro["descripcion"],
                    "tamaño": perro["tamaño"],
                    "genero": perro["genero"]}
                
                    for perro in data]
        else:
            print("Error al obtener los datos:", response.status_code)
            return []
    except Exception as e:
        print("Error en la conexión:", e)
        return []

async def create_perro(json_nombre, raza, edad, estadosalud, color, descripcion, tamaño, genero, imagen):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:80/perrosgod/addperro", json={"nombre": json_nombre, "raza": raza, "edad": edad, "estadosalud": estadosalud, "color": color, "imagen": imagen, "descripcion": descripcion, "tamaño": tamaño, "genero": genero })
        
        if response.status_code == 201:
            print("Perro creado:", response.json())
        else:
            print("Error al crear el perro:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def update_perro(perro_id, ud_nombre, ud_raza, ud_estadoSalud, ud_color, ud_imagen, ud_descripcion, ud_tamaño, ud_genero):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://localhost:80/perrosgod/editperro/{perro_id}", json={"nombre":ud_nombre , "raza": ud_raza , "estadoSalud": ud_estadoSalud , "color": ud_color , "imagen": ud_imagen, "descripcion": ud_descripcion, "tamaño": ud_tamaño, "genero": ud_genero})
        
        if response.status_code == 200:
            print("Usuario perro:", response.json())
        else:
            print("Error al actualizar el perro:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def delete_perro(perro_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://localhost:80/perrosgod/deleteperro/{perro_id}")
        
        if response.status_code == 200:
            print("Perro eliminado:", response.json())
        else:
            print("Error al eliminar el perro:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)
        
def get_items():
    return items

def add_item(item):
    items.append(item)
    
def edit_item(index, new_item):
    items[index] = new_item

def delete_item(index):
    items.pop(index)
