"""
Modulo que contiene la responsabilidad de guardar las seniales, adquiridas y procesadas
en algun tipo de almacen de persistencia (archivo plano, xml, base de dato)
"""
import os
import pickle
from typing import Any


class PersistidorPickle:
    """
    Clase de persistidor que persiste un tipo de objeto de manera serializada
    """

    def __init__(self, recurso: str):
        """
        Se crea el archivo con el path donde se guardarán los archivos
        de las entidades a persistir.
        :param recurso: Path del repositorio de entidades.
        """
        self._recurso = recurso
        if not os.path.isdir(recurso):
            os.mkdir(recurso)

    def persistir(self, entidad: Any, nombre_entidad: str) -> None:
        """
        Se persiste el objeto (entidad) y se indica el tipo de entidad.
        :param entidad: Objeto a persistir.
        :param nombre_entidad: Nombre del archivo donde se guardará la entidad.
        """
        archivo = f"{nombre_entidad}.pickle"
        ubicacion = os.path.join(self._recurso, archivo)
        try:
            with open(ubicacion, "wb") as archivo:
                pickle.dump(entidad, archivo)
        except IOError as e:
            print(f"Error al guardar la entidad: {e}")

    def recuperar(self, id_entidad: str) -> Any:
        """
        Se lee la entidad a tratar.
        :param id_entidad: Identificador de la entidad a recuperar.
        :return: Entidad recuperada.
        """
        archivo = f"{id_entidad}.pickle"
        ubicacion = os.path.join(self._recurso, archivo)
        try:
            with open(ubicacion, "rb") as archivo:
                return pickle.load(archivo)
        except (IOError, ValueError) as e:
            print(f"Error al recuperar la entidad: {e}")
            return None