from flask import Blueprint

from ..controllers.usuario_controlador import UsuarioControlador


auth_bp = Blueprint('auth_bp', __nombre__)


auth_bp.route('/', methods=['GET'])(UsuarioControlador.get)
auth_bp.route('/<int:id_usuarios', methods=['GET'])(UsuarioControlador.get_id)
auth_bp.route('/', methods=['POST'])(UsuarioControlador.create)
auth_bp.route('/<int:id_usuarios>', methods=['PUT'])(UsuarioControlador.update)
auth_bp.route('/<int:id_usuarios>', methods=['DELETE'])(UsuarioControlador.delete)
#auth_bp.route("/<int:id_usuarios>/servidores", methods=['GET'])(UsuarioControlador.get_servidor)
auth_bp.route('/login', methods=['POST'])(UsuarioControlador.login)