from ..models.servidores.servidor_model import Servidor 
from flask import request, session

class ServidorControlador:

    @classmethod
    def get(cls):
        servidores = []
        for servidor in Servidor.get():
            servidores.append(servidor.serialize())
        return servidores, 200


    @classmethod
    def get_usuario_servidores(cls):
        from ..models.auth import Usuario 

        usuario = Usuario(id_usuarios=session["id_servidores"])
        servidores = []
        for servidor in Servidor.get():
            servidores.append(servidor.serialize())
        return jsonify(servidores), 200


    @classmethod
    def get_id(cls, id_servidores):
        servidor = Servidor(id_servidores=id.servidores)
        servidor = Servidor.get(servidor)
        if servidor:
            return servidor.serialize(), 200


    @classmethod
    def create(cls):
        data = request.json
        servidor = Servidor(
            id_servidores = data.get('id_servidores'), #
            nombre = data.get('nombre'),
            imagen = data.get('imagen'),
            descripcion = data.get('descripcion')
        )
    Servidor.create(servidor)
    return {'message': 'Servidor creado con éxito'}, 201


    @classmethod
    def update(cls, id_servidores):
        data = request.json
        servidor = Servidor(
            id_servidores=id_servidores,
            nombre=data.get('nombre'),
            imagen=data.get('imagen'),
            descripcion=data.get('descripcion'),
        )
        

    
    @classmethod
    def delete(cls, id_servidores):
        servidor = Servidor.get(id_servidores)
        if Servidor.is_registered(servidor):
            Servidor.delete(servidor)
            return {'message': 'Servidor eliminado correctamente'}, 204


    @classmethod
    def get_usuarios(cls, id_servidores):
        servidor = Servidor(id_servidores=id_servidores)
        usuarios = []
        for usuario in Servidor.get_usuarios(servidor):
            usuarios.append(usuario.serialize())
        return usuarios, 200

    

    def usuario_registrado(cls, id_servidores):
        data = request.json
        servidor = Servidor(id_servidores=id_servidores)
        from ..models.auth import Usuario 

        id_usuarios = session["id_usuarios"]
        usuario = Usuario(id_usuarios=data.get("id_usuarios"))
        Servidor.usuario_registrado(usuario, servidor)
        return {"message": "Usuario registrado exitosamente"}, 200

    

    
