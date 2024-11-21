import httpx
import requests

items = []  # Inicializa la variable global

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
            response = await client.get("http://localhost:80/Usersockets/index")
        print(f"Entra a listar 1 {response.status_code}")

        if response.status_code == 200:
            users = response.json()
            print(f"Entra a listar {users}")
            
            data = response.json()
            return [{"id": user["id"], 
                     "name": user["name"],
                     "pass": user["pass"]} 
                    for user in data]
        else:
            print("Error al obtener los datos:", response.status_code)
            return []
    except Exception as e:
        print("Error en la conexión:", e)
        return []

async def create_user(name, password):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:80/Usersockets/add", json={"nameUser": name, "passwordUser": password})
        
        if response.status_code == 201:
            print("Usuario creado:", response.json())
        else:
            print("Error al crear el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def update_user(user_id, new_name, new_password):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://localhost:80/Usersockets/update/{user_id}", json={"nameUser": new_name, "passwordUser": new_password})
        
        if response.status_code == 200:
            print("Usuario actualizado:", response.json())
        else:
            print("Error al actualizar el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def delete_user(user_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://localhost:80/Usersockets/delete/{user_id}")
        
        if response.status_code == 200:
            print("Usuario eliminado:", response.json())
        else:
            print("Error al eliminar el usuario:", response.status_code)
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
