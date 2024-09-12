from abc import ABCMeta, abstractmethod
from typing import Any

class BaseTrazador(metaclass=ABCMeta):
    """
    Clase base abstracta para trazadores.
    """

    @abstractmethod
    def trazar(self, entidad: Any, accion: str, mensaje: str) -> None:
        """
        Método abstracto para trazar una acción sobre una entidad.
        :param entidad: Entidad a trazar.
        :param accion: Acción realizada.
        :param mensaje: Mensaje de traza.
        """
        pass