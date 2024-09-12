from abc import ABCMeta, abstractmethod
from typing import Any

class BaseAuditor(metaclass=ABCMeta):
    """
    Clase base abstracta para auditores.
    """

    @abstractmethod
    def auditar(self, entidad: Any, auditoria: str) -> None:
        """
        Método abstracto para auditar una entidad.
        :param entidad: Entidad a auditar.
        :param auditoria: Información de auditoría.
        """
        pass