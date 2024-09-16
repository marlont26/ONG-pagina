from app import create_app, db, crear_admin_default
import os

app = create_app()

# Crear las tablas en la base de datos si no existen
with app.app_context():
    db.create_all()

# Crear el administrador por defecto
crear_admin_default()  # Llamar a la función para crear admin

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))