from ...database import DatabaseConnection

class Canal:
    """Canal modelo class"""

    def __init__(self, **kwargs):
        self.id_canales = kwargs.get('id_canales')
        self.nombre = kwargs.get('nombre')
        self.id_servidor = kwargs.get('id_servidor')


    @classmethod
    def crear(cls, canal):
        query= """INSERT INTO msjbox.canales (nombre, id_servidor) 
        VALUES (%(nombre)s, %(id_del_servidor)s);"""

        params = canal.__dict__
        DatabaseConnection.execute(query, params=params)

    @classmethod
    def get_all(cls, id_servidor):
        query = """SELECT * FROM msjbox.canales WHERE id_servidor = %(id_servidor)s;"""
        params = {'id_servidor': id_servidor}
        results = DatabaseConnection.fetch_all(query, params=params)

        canales = []
        for result in results:
            canales.append(cls(
                id_canales = result[0],
                nombre = result[1],
                id_servidor = result[2]
            ))
        return canales

    @classmethod
    def update(cls, canales):
        allowed_columns = {'nombre', 'id_servidores'}
        query_parts = []
        params = []
        for key, value in canales.__dict__.items():
            if key in allowed.columns and value is not None:
                query_parts.append(f"{key} = %s")
                params.append(value)
            params.append(canales.id_canales)
            query = "UPDATE mjsbox.canales SET" + ", ".join(query_parts) + " WHERE id_canales = %s"
            DatabaseConnection.execute_query(query=params)

    @classmethod
    def get(cls, id_canales):
        query = """SELECT * FROM msjbox.canales WHERE id_canales = %(id_canales)s;"""
        params = {'id_canales': id_canales}
        result = DatabaseConnection.fetch_one(query, params=params)

        if result is not None:
            return cls(
                id_canales = result
            )

    @classmethod
    def delete(cls, canales):
        query = """DELETE FROM msjbox.canales WHERE id_canales=%S"""
        params = canales.id_canales,
        DatabaseConnection.execute_query(query, params=params)