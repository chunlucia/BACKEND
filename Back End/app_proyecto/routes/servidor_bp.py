from flask import Blueprint
from ..controllers.servidor_controlador import ServidorControlador


servidor_bp = Blueprint('servidor_bp', __name__)

servidor_bp.route('/create', methods=['POST'])(ServidorControlador.create)
servidor_bp.route('/', methods=['GET'])(ServidorControlador.show_servers)
servidor_bp.route('/<int:id_servidores>', methods=['GET'])(ServidorControlador.get)
servidor_bp.route('/<int:id_servidores>', methods=['PUT'])(ServidorControlador.update)
servidor_bp.route('/<int:id_servidores>', methods=['DELETE'])(ServidorControlador.delete)
servidor_bp.route('/uxs', methods=['POST'])(ServidorControlador.add_user_server)
servidor_bp.route('/uxs', methods=['GET'])(ServidorControlador.get_uxs)
