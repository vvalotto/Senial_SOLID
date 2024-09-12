"""
Modulo que contiene la responsabilidad de guardar las seniales, adquiridas y procesadas
en algun tipo de almacen de persistencia (archivo plano, xml, base de dato)
"""
import os
import pickle
from abc import ABC, abstractmethod
from persistidor.mapeador import MapeadorArchivo
from typing import Any

class BaseContexto(ABC):
    """
    Clase abstract que define la interfaz de la persistencia de datos
    """
    def __init__(self, recurso):
        """
        Se crea el contexto, donde el nombre es el recurso fisico donde residen los datos
        junto con esto se crea el recurso fisico con el nombre
        :param recurso: Path del repositorio de entidades.
        """
        if not recurso:
            raise ValueError("Nombre de recurso vacío")
        self._recurso = recurso
        if not os.path.isdir(recurso):
            os.mkdir(recurso)

    @property
    def recurso(self) -> str:
        return self._recurso

    @abstractmethod
    def persistir(self, entidad: Any, id_entidad: str) -> None:
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es el tipo a persistir
        """
        pass

    @abstractmethod
    def recuperar(self, id_entidad: str, entidad: Any) -> Any:
        """
        Se identifica a la instancia de la entidad con nombre_entidad y en entidad es devuelta por el metodo
        """
        pass

class ContextoPickle(BaseContexto):
    """
    Clase de persistidor que persiste un tipo de objeto de manera serializada
    """

    def persistir(self, entidad: Any, id_entidad: str) -> None:
        """
        Se persiste el objeto (entidad) y se indica el tipo de entidad.
        :param entidad: Objeto a persistir.
        :param id_entidad: Nombre del archivo donde se guardará la entidad.
        """
        archivo = f"{id_entidad}.pickle"
        ubicacion = os.path.join(self._recurso, archivo)
        try:
            with open(ubicacion, "wb") as archivo:
                pickle.dump(entidad, archivo)
        except IOError as e:
            print(f"Error al guardar la entidad: {e}")

    def recuperar(self, id_entidad: str, entidad: Any) -> Any:
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

class ContextoArchivo(BaseContexto):
    """
    Contexto del recurso de persistencia de tipo archivo
    """


    def persistir(self, entidad: Any, id_entidad: str) -> None:
        """
        Agregar un objeto (entidad) para persistirlo.
        :param entidad: Tipo de entidad.
        :param id_entidad: Identificación de la instancia de la entidad.
        """
        mapeador = MapeadorArchivo()
        archivo = f"{id_entidad}.dat"
        contenido = mapeador.ir_a_persistidor(entidad)
        ubicacion = os.path.join(self._recurso, archivo)

        try:
            with open(ubicacion, "w") as archivo:
                archivo.write(contenido)
        except IOError as e:
            print(f"Error al guardar la entidad: {e}")

    def recuperar(self, entidad, id_entidad):
        """
        Obtiene la entidad guardada.
        :param id_entidad: Identificación de la entidad a recuperar.
        :return: Entidad recuperada.
        """
        archivo = f"{id_entidad}.dat"
        ubicacion = os.path.join(self._recurso, archivo)
        contenido = ''
        try:
            with open(ubicacion, "r") as archivo:
                contenido = archivo.read()
            mapeador = MapeadorArchivo()
            return mapeador.venir_desde_persistidor(entidad, contenido)
        except IOError as e:
            print(f"Error al recuperar la entidad: {e}")
            return None
        except ValueError as e:
            print(f"Error de valor al recuperar la entidad: {e}")
            return None
