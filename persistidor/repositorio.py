"""
Patrón repositorio: responsable de manejar de manera abstracta la persitencia
de las entidades
"""
from abc import ABC, abstractmethod
from typing import Any


class BaseRepositorio(ABC):
    """
    Define la interfaz para el acceso a la persistencia de datos
    """
    def __init__(self, contexto: Any):
        """
        Inicializa el repositorio con un contexto de persistencia
        :param contexto: Contexto de persistencia
        """
        self._contexto = contexto

    @abstractmethod
    def guardar(self, entidad: Any) -> None:
        """
        Persiste la entidad
        :param entidad: Entidad a persistir
        """
        pass

    @abstractmethod
    def obtener(self, entidad: str, id_entidad: str) -> Any:
        """
        Obtiene una entidad por su identificador
        :param id_entidad: Identificador de la entidad
        :return: Entidad recuperada
        """
        pass


class RepositorioSenial(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia de señales
    """
    def __init__(self, contexto: Any):
        """
        Inicializa el repositorio con un contexto de persistencia
        :param contexto: Contexto de persistencia
        """
        super().__init__(contexto)

    def guardar(self, senial: Any) -> None:
        """
        Persiste la señal
        :param senial: Señal a persistir
        """
        try:
            self._contexto.persistir(senial, senial.id)
        except Exception as e:
            print(f"Error al guardar la señal: {e}")
            raise

    def obtener(self, senial: Any, id_senial: str) -> Any:
        """
        Obtiene una señal por su identificador
        :param id_senial: Identificador de la señal
        :return: Señal recuperada
        """
        try:
            return self._contexto.recuperar(senial, id_senial)
        except Exception as e:
            print(f"Error al obtener la señal: {e}")
            raise

class RepositorioUsuario(BaseRepositorio):
    """
    Repositorio para gestionar la persistencia de usuarios
    """
    def __init__(self, contexto: Any):
        """
        Inicializa el repositorio con un contexto de persistencia
        :param contexto: Contexto de persistencia
        """
        super().__init__(contexto)

    def guardar(self, usuario: Any) -> None:
        """
        Persiste el usuario
        :param usuario: Usuario a persistir
        """
        try:
            self._contexto.persistir(usuario, usuario.id)
        except Exception as e:
            print(f"Error al guardar el usuario: {e}")
            raise

    def obtener(self, usuario: Any, id_usuario: str) -> Any:
        """
        Obtiene un usuario por su identificador
        :param id_usuario: Identificador del usuario
        :return: Usuario recuperado
        """
        try:
            return self._contexto.recuperar(usuario, id_usuario)
        except Exception as e:
            print(f"Error al obtener el usuario: {e}")
            raise