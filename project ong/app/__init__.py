from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    login_manager.login_view = 'usuario.login'
    login_manager.login_message = "Por favor, inicia sesión para acceder a esta página."

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import Usuario
        return Usuario.query.get(int(user_id))

    from app.routes import (
        cuidado_routes, 
        empleado_routes, 
        perro_routes, 
        solicitudAdopcion_routes, 
        veterinario_routes, 
        visitaMedica_routes, 
        main_routes, 
        usuario_routes,
        adoptante_routes,
        mensaje_contacto_routes
    )

    app.register_blueprint(adoptante_routes.bp)
    app.register_blueprint(cuidado_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(perro_routes.bp)
    app.register_blueprint(solicitudAdopcion_routes.bp)
    app.register_blueprint(veterinario_routes.bp)
    app.register_blueprint(visitaMedica_routes.bp)
    app.register_blueprint(main_routes.bp)
    app.register_blueprint(usuario_routes.bp)
    app.register_blueprint(mensaje_contacto_routes.bp)

    return app