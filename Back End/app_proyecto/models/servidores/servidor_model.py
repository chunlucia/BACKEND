from ...database import DatabaseConnection

class Servidor:
    """Servidor modelo class"""

    def __init__(self, **kwargs):
        self.id_servidores = kwargs.get('id_servidores')
        self.nombre = kwargs.get('nombre')
        self.imagen = kwargs.get('imagen')
        self.descripcion = kwargs.get('descripcion')
    
    @classmethod
    def create(cls, servidor):
        query = """INSERT INTO msjbox.servidores (id_servidores, nombre, imagen, descripcion)
        VALUES (%(id_servidores)s, %(nombre)s, %(imagen)s, %(descripcion)s);""" 
    
        params = servidor.__dict__
        DatabaseConnection.execute(query, paramas=params)

    @classmethod
    def get(cls,id_servidores):
        query = """SELECT * FROM msjbox.servidores WHERE id_servidores = %(id_servidores)s;"""
        params = {'id_servidores': id_servidores}
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_servidores= result[0],
                nombre= result[1],
                imagen= result[2],
                descripcion= result[3]
            )
        return None

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM msjbox.servidores"""
        results = DatabaseConnection.fetch_all(query)

        servidores = []
        if result in results:
            servidores.append(cls(*result))
        return servidores

    def serialize(self):
        """Serialize object representation"""
        return{
            "id_servidores": self.id_servidores,
            "nombre": self.nombre,
            "imagen": self.imagen,
            "descripcion": self.descripcion
        }

    @classmethod 
    def update(cls, servidor):
        allowed_columns = {'id_servidores', 'nombre', 'imagen', 'descripcion'}
        query_parts = []
        params = []
        for key, value in servidor.__dict__.items():
            if key in allowed_columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
        params.append(servidor.id_servidores)

        query = "UPDATE msjbox.servidores SET "+", ".join(query_parts) + "WHERE id_servidores = %s"
        DatabaseConnection.execute_query(query, params=params)

    @classmethod
    def delete(cls, servidor):
        query = """DELETE FROM msjbox.servidores WHERE id_servidores = %s"""
        params = servidor.id_servidores,
        DatabaseConnection.execute_query(query, params=params)
