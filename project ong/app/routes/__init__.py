from flask import Blueprint

bp = Blueprint('main',__name__)

from app.routes import adoptante_routes, cuidado_routes, donacion_routes, donante_routes, empleado_routes, perro_routes, solicitudAdopcion_routes, veterinario_routes, visitaMedica_routes