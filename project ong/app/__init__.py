from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'usuario.login'

    @login_manager.user_loader
    def load_user(id):
        from .models.usuario import Usuario
        return Usuario.query.get(int(id))

    from app.routes import (
        adoptante_routes, 
        cuidado_routes, 
        empleado_routes, 
        perro_routes, 
        solicitudAdopcion_routes, 
        veterinario_routes, 
        visitaMedica_routes, 
        main_routes, 
        usuario_routes
    )

    # Registrar blueprints
    app.register_blueprint(adoptante_routes.bp)
    app.register_blueprint(cuidado_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(perro_routes.bp)
    app.register_blueprint(solicitudAdopcion_routes.bp)
    app.register_blueprint(veterinario_routes.bp)
    app.register_blueprint(visitaMedica_routes.bp)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(usuario_routes.bp)

    return app
