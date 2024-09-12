"""
Patrón repositorio: responsable de manejar de manera abstracta la persitencia
de las entidades
"""
from abc import ABC, abstractmethod
from typing import Any
import datetime

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
        :param entidad: Tipo de la entidad
        :param id_entidad: Identificador de la entidad
        :return: Entidad recuperada
        """
        pass

    @abstractmethod
    def auditar(self, entidad, auditoria):
        """
        Realiza el registro de auditoría sobre la entidad indicada
        :param entidad: Entidad a auditar
        :param auditoria: Información de auditoría
        """
        pass

    @abstractmethod
    def trazar(self, entidad, acción, mensaje):
        """
        Realiza la traza del evento ocurrido sobre la entidad y con el mensaje de
        traza correspondiente
        :param entidad: Entidad a trazar
        :param accion: Acción realizada
        :param mensaje: Mensaje de traza
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

    def auditar(self, senial, auditoria):
        """
        Realiza el registro de auditoría sobre la señal indicada
        :param senial: Señal a auditar
        :param auditoria: Información de auditoría
        """
        nombre = 'auditor.log'
        try:
            with open(nombre, 'a') as auditor:
                auditor.writelines('------->\n')
                auditor.writelines(str(senial) + '\n')
                auditor.writelines(str(datetime.datetime.now()) + '\n')
                auditor.writelines(str(auditoria) + '\n')
        except IOError as eIO:
            print(f"Error al auditar la señal: {eIO}")
            raise

    def trazar(self, senial, accion, mensaje):
        """
        Realiza la traza del evento ocurrido sobre la señal y con el mensaje de
        traza correspondiente
        :param senial: Señal a trazar
        :param accion: Acción realizada
        :param mensaje: Mensaje de traza
        """
        nombre = 'logger.log'
        try:
            with open(nombre, 'a') as logger:
                logger.writelines('------->\n')
                logger.writelines('Accion: ' + str(accion))
                logger.writelines(str(senial) + '\n')
                logger.writelines(str(datetime.datetime.now()) + '\n')
                logger.writelines(str(mensaje) + '\n')
        except IOError as eIO:
            print(f"Error al trazar la señal: {eIO}")
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

    def auditar(self, entidad, auditoria):
        """
        Realiza el registro de auditoría sobre el usuario indicado
        :param usuario: Usuario a auditar
        :param auditoria: Información de auditoría
        """
        raise ("Auditar, Metodo No implementado")


    def trazar(self, entidad, acción, mensaje):
        """
        Realiza la traza del evento ocurrido sobre el usuario y con el mensaje de
        raza correspondiente
        :param usuario: Usuario a trazar
        :param accion: Acción realizada
        :param mensaje: Mensaje de traza
        """
        raise NotImplementedError("Método no implementado")