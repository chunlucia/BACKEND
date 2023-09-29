from ..models.auth.usuario_model import Usuario 
from flask import request, session, json

class UsuarioController:

    @classmethod
    def get(cls):
        usuarios = []
        for usuarios in Usuario.get():
            usuarios.append(usuario.serialize())
        return usuarios, 200

    
    @classmethod
    def get_id(cls, id_usuarios):
        usuario = Usuario(id_usuarios=id.usuarios)
        usuario = Usuario.get(usuario)
        if usuario:
            return usuario.serialize(), 200


    @classmethod
    def create(cls):
        data = request.json
        usuario = Usuario(
            id_usuarios=data.get("id_usuarios"),
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            fecha_nacimiento=data.get("fecha_nacimiento"),
            email=data.get("email"),
            nombre_usuario=data.get("nombre_usuario"),
            contrasena=data.get("contrasena"),
            imagen=data.get("imagen"),
        )
        Usuario.create(usuario)
        return {"message": "Usuario creado con éxito"}, 201


    @classmethod
    def update(cls, id_usuarios):
        data = request.json
        usuario = Usuario(
            id_usuarios=id_usuarios,
            nombre=data.get("nombre"),
            apellido=data.get("apellido"),
            fecha_nacimiento=data.get("fecha_nacimiento"),
            email=data.get("email"),
            nombre_usuario=data.get("nombre_usuario"),
            contrasena=data.get("contrasena"),
            imagen=data.get("imagen"),
        )


    @classmethod
    def login(cls):
        data = request.json
        usuario = Usuario(
            nombre_usuario = data.get('nombre_usuario'),
            contrasena = data.get('contrasena')
        )
        print(user.serialize())
        usuario = Usuario.login(usuario)
        if usuario:
            session['id_usuarios'] = usuario.id_usuarios
            session['nombre'] = usuario.nombre
            session['apellido'] = usuario.apellido
            session['fecha_nacimiento'] = usuario.fecha_nacimiento
            session['email'] = usuario.email
            session['nombre_usuario'] = usuario.nombre_usuario
            session['contrasena'] = usuario.contrasena
            session['imagen'] = usuario.imagen
            return usuario.serialize(), 200
        return {"messaje": "Usuario o contraseña incorrectos, por favor vuelve a escribirlos"}, 401
  



