from ..models.canales.canal_model import Canal

from flask import request, session

class CanalControlador:

    @classmethod
    def get(cls):
        canales = []
        for canal in Canal.get():
            canales.append(canal.serialize())
        return canales, 200


    @classmethod
    def get_id(cls, id_canales):
        canal = Canal(id_canales=id.canales)
        canal = Canal.get(canal)
        if canal:
            return canal.serialize(), 200


    @classmethod
    def create(cls):
        data = request.json
        canal = Canal(
            id_canales=data.get("id_canales"),
            nombre=data.get("nombre"),
            id_servidor=data.get("id_servidor"),
        )
        Canal.create(canal)
        return {"message": "Canal creado con éxito"}, 201


    @classmethod
    def update(cls, id_canales):
        data = request.json
        canal = Canal(
            id_canales=data.get("id_canales"),
            nombre=data.get("nombre"),
            id_servidor=data.get("id_servidor"),
        )


    @classmethod
    def delete(cls, id_canales):
        canal = Canal.get(id_canales)
        if Canal.is_registered(canal):
            canal.delete(canal)
            return {'message': 'Canal eliminado correctamente'}, 204