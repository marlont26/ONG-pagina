import httpx
import requests

items = []

async def preload_items():
    global items
    print("Preloading items --------------------------------")
    items = await get_item2()
    return items

async def get_item2():
    try:
        print("Entra a listar")
        async with httpx.AsyncClient() as client:
            response = await client.get("http://localhost:80/usuariosgod/usuarios")
        print(f"Entra a listar 1 {response.status_code}")

        if response.status_code == 200:
            usuarios = response.json()
            print(f"Entra a listar {usuarios}")
            
            data = response.json()
            return [{
                "id": usuario["id"],
                "nombre": usuario["nombre"],
                "apellido": usuario["apellido"],
                "email": usuario["email"],
                "telefono": usuario["telefono"],
                "cedula": usuario["cedula"],
                "rol": usuario["rol"]
            } for usuario in data]
        else:
            print("Error al obtener los datos:", response.status_code)
            return []
    except Exception as e:
        print("Error en la conexión:", e)
        return []

async def create_usuario(nombre, apellido, email, password, telefono, cedula, rol):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:80/usuariosgod/addusuario", 
                json={
                    "nombre": nombre,
                    "apellido": apellido,
                    "email": email,
                    "password": password,
                    "telefono": telefono,
                    "cedula": cedula,
                    "rol": rol
                })
        
        if response.status_code == 201:
            print("Usuario creado:", response.json())
        else:
            print("Error al crear el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def update_usuario(usuario_id, nombre, apellido, email, telefono, cedula, rol, password=None):
    try:
        data = {
            "nombre": nombre,
            "apellido": apellido,
            "email": email,
            "telefono": telefono,
            "cedula": cedula,
            "rol": rol
        }
        if password:
            data["password"] = password

        async with httpx.AsyncClient() as client:
            response = await client.put(f"http://localhost:80/usuariosgod/editusuario/{usuario_id}", 
                json=data)
        
        if response.status_code == 200:
            print("Usuario actualizado:", response.json())
        else:
            print("Error al actualizar el usuario:", response.status_code)
    except Exception as e:
        print("Error en la conexión:", e)

async def delete_usuario(usuario_id):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.delete(f"http://localhost:80/usuariosgod/deleteusuario/{usuario_id}")
        
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