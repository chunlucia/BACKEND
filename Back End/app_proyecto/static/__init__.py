from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from datetime import datetime
from flask import Flask, requests
from .database import DatabaseConnection


def init_app():
    """Crea y configura la aplicación Flask"""

    app = Flask(
        __name__,
        static_folder=Config.STATIC_FOLDER, 
        template_folder=Config.TEMPLATE_FOLDER,
    )

    CORS(app, supports_credentials=True)

    app.config.from_object(Config)
    DatabaseConnection.set_confid(app.config)

    app.register_blueprint(canal_bp, url_prefix = '/canal')
    app.register_blueprint(mensajes_bp, url_prefix = '/mensajes')
    app.register_blueprint(servidores_bp, url_prefix = '/servidores')
    app.register_blueprint(usuario_bp, url_prefix = 'usuario')
    
    return app
    