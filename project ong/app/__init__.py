from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)

    from app.routes import adoptante_routes, cuidado_routes, donacion_routes, donante_routes, empleado_routes, perro_routes, solicitudAdopcion_routes, veterinario_routes, visitaMedica_routes
    app.register_blueprint(adoptante_routes.bp)
    app.register_blueprint(cuidado_routes.bp)
    app.register_blueprint(donacion_routes.bp)
    app.register_blueprint(donante_routes.bp)
    app.register_blueprint(empleado_routes.bp)
    app.register_blueprint(perro_routes.bp)
    app.register_blueprint(solicitudAdopcion_routes.bp)
    app.register_blueprint(veterinario_routes.bp)
    app.register_blueprint(visitaMedica_routes.bp)

    return app  