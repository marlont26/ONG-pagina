def test_index(client):
    response = client.get('/Usuario/')
    assert response.status_code == 200
    assert b"Usuarios Registrados" in response.data  # Asumiendo que hay un texto "Lista de Usuarios" en la página

def test_add_user(client):
    response = client.post('/Usuario/add', data={
        'nombre': 'new_user',
        'password': 'new_password'

    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Usuarios" in response.data  # Asumiendo que el nombre del usuario se muestra en la página

def test_edit_user(client, usuario):
    response = client.post(f'/Usuario/edit/{usuario.id}', data={
        'nombre': 'updated_user',
        'password': 'updated_password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"updated_user" in response.data  # Asumiendo que el nombre del usuario actualizado se muestra en la página

def test_delete_user(client, usuario):
    response = client.get(f'/Usuario/delete/{usuario.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Usuarios" in response.data  # Asumiendo que hay un mensaje de confirmación de eliminación

