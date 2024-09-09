from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Carga la configuración desde config.py
    
    db.init_app(app)

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
