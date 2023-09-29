from ...database import DatabaseConnection

class Usuario:
    """Usuario modelo clase"""

    _keys = ["id_usuarios", "nombre_usuario", "nombre", "apellido", "fecha_nacimiento", "email", "contrasena", "imagen"]

    def __init__(self, **kwargs):
        self.id_usuarios = kwargs.get('id_usuarios')
        self.nombre_usuario = kwargs.get('nombre_usuario')
        self.nombre = kwargs.get('nombre')
        self.apellido = kwargs.get('apellido')
        self.fecha_nacimiento = kwargs.get('fecha_nacimiento')
        self.email = kwargs.get('email')
        self.contrasena = kwargs.get('contrasena')
        self.imagen = kwargs.get('imagen')



    def serialize(self):

            return{
                "id_usuarios": self.id_usuarios,
                "nombre_usuario": self.nombre_usuario,
                "nombre": self.nombre,
                "apellido": self.apellido,
                "fecha_nacimiento": self.fecha_nacimiento,
                "email": self.email,
                "contrasena": self.contrasena,
                "imagen": self.imagen,
            }

    
    @classmethod
    def create(cls, usuario):
        query = """INSER INTO msjbox.usuarios (nombre, apellido, fecha_nacimiento, email, nombre_usuario, contrasena, imagen)
        VALUES (%(nombre)s, %(apellido)s, %(fecha_nacimiento)s, %(email)s, %(nombre_usuario)s, %(contrasena)s, %(imagen)s)"""
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)


    @classmethod
    def delete(cls, usuario):
        query = "DELETE FROM msjbox.usuarios WHERE id_usuarios = %(id_usuarios)s"
        params = usuario.__dict__
        DatabaseConnection.execute_query(query, params)


    @classmethod
    def get(cls, usuario=None):
        if usuario is not None and usuario.id_usuarios is not None:
            query = """SELECT id_usuarios, nombre, apellido, fecha_nacimiento, email, nombre_usuario, contrasena, imagen
            FROM msjbox.usuarios WHERE id_usuarios = %(id_usuarios)s"""
            params = user.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = "SELECT id_usuarios, nombre, apellido, fecha_nacimiento, email, nombre_usuario, contrasena, imagen FROM msjbox.usuarios"
            results = DatabaseConnection.execute.fetch_all(query)
            usuarios = []
            for row in results:
                usuarios.append(cls(**dict(zip(cls._keys, row))))
            return usuarios


    @classmethod
    def update(cls, usuario):
        query = "UPDATE msjbox.usuarios SET"
        usuario_data = usuario.__dict__
        usuario_updates = []
        for key in usuario_data.keys():
            if usuario_data[key] is not None and key != "id_usuarios":
                usuario_updates.append(f"{key} = %({key})s")
        query += ", ".join(usuario_updates)
        query += "WHERE id_usuarios = %(id_usuarios)s"
        DatabaseConnection.execute_query(query, usuario_data)


    #@classmethod
    #def get_servidor(cls, usuario):
        #query = """SELECT servidores.id_servidores, servidores.nombre, servidores.imagen, servidores.descripcion
        #FROM msjbox.servidores"""
    
    @classmethod
    def login(cls, usuario):
        query = """SELECT id_usuarios, nombre, apellido, fecha_nacimiento, email, nombre_usuario, contrasena, imagen
        FROM msjbox.usuarios WHERE nombre_usuario = %(nombre_usuario)s AND contrasena = %(contrasena)s"""
        params = usuario.__dict__
        result = DatabaseConnection.fetch_one(query, params)
        if result:
            return cls(**dict(zip(cls._keys, result)))
        else:
            return None


    