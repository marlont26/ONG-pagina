from flask import Blueprint

bp = Blueprint('main',__name__)

from app.routes import cuidado_routes,  empleado_routes, perro_routes, solicitudAdopcion_routes, veterinario_routes, visitaMedica_routes, usuario_routes