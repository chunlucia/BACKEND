from flask import Blueprint
from ..controllers.canal_controlador import CanalControlador 

canal_bp = Blueprint('canal_bp', __name__)

canal_bp.route('/<int:id_canales>', methods=['GET'])(CanalControlador.get)
canal_bp.route('/', methods=['GET'])(CanalControlador.get_all)
canal_bp.route('/create', methods=['POST'])(CanalControlador.create)
canal_bp.route('/<int:id_canales>', methods=['PUT'])(CanalControlador.update)
canal_bp.route('/<int:id_canales>', methods=['DELETE'])(CanalControlador.delete)