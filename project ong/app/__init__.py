from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Carga la configuración desde config.py
    
    db.init_app(app)
    
    # Inicializar el LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app)

    # Configura la vista de login
    login_manager.login_view = 'usuario_routes.login'  # Cambia esto por la ruta de tu vista de login
    login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."

    # Cargar usuario (se usa para la sesión de usuario)
    from app.models import Usuario  # Asegúrate de importar tu modelo de usuario correctamente

    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))

    # Registrar Blueprints
    from app.routes import (
        cuidado_routes, 
        empleado_routes, 
        perro_routes, 
        solicitudAdopcion_routes, 
        veterinario_routes, 
        visitaMedica_routes, 
        main_routes, 
        usuario_routes
    )
    
    app.register_blueprint(cuidado_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(perro_routes.bp)
    app.register_blueprint(solicitudAdopcion_routes.bp)
    app.register_blueprint(veterinario_routes.bp)
    app.register_blueprint(visitaMedica_routes.bp)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(usuario_routes.bp)

    return app
