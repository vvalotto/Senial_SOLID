"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio

Modificacion: Se crea un clase abstracta que define todas las interfaces de las
estructuras de las seniales y resuelve la violacion de los principio OCP y LSP
"""
from abc import abstractmethod, ABC
from typing import Any, List


class SenialBase(ABC):

    def __init__(self, tamanio: int = 10):
        """
        Constructor: Inicializa la lista de valores vacía.
        :param tamanio: Tamaño inicial de la señal.
        """
        self._valores: List[]= []
        self._fecha_adquisicion: Any = None
        self._cantidad: int = 0
        self._tamanio: int= tamanio

    # Propiedades
    @property
    def fecha_adquisicion(self) -> Any:
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor: Any) -> None:
        self._fecha_adquisicion = valor

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        self._cantidad = valor

    @property
    def tamanio(self) -> int:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor : int)-> None:
        self._tamanio = valor

    @property
    def valores(self) -> List[float]:
        return self._valores

    @valores.setter
    def valores(self, datos: List[float]) -> None:
        self._valores = datos

    @abstractmethod
    def poner_valor(self, valor: float) -> None:
        pass

    @abstractmethod
    def sacar_valor(self) -> Any:
        pass

    def limpiar(self) -> None:
        """
        Deja a la senial sin valores
        """
        self._valores.clear()
        self._cantidad = 0


    def obtener_valor(self, indice: int) -> Any:
        """
        Recupera el contenido según el indice
        :param indice:
        :return: Valor
        """
        try:
            return self._valores[indice]
        except IndexError:
            print(f'Error: Índice {indice} fuera de rango')
            return None

    def obtener_tamanio(self) -> int:
        """
        Retorna el largo de la lista de valores.
        :return: Tamaño de la lista de valores.
        """
        return len(self._valores)

    def obtener_valores(self) -> List[float]:
        """
        Retorna la lista de valores.
        :return: Lista de valores.
        """
        return self._valores

    def poner_valores(self, valores: List[float]) -> None:
        """
        Agrega una lista de valores a la lista de la señal
        :param valores: lista de valores a agregar
        """
        self._valores = valores
        
    def __str__(self) -> str:
        cad = ""
        cad += 'Tipo: ' + str(type(self)) + '\n'
        cad += 'fecha_adquisicion: ' + str(self._fecha_adquisicion)
        return cad
    
class SenialLista(SenialBase):
    pass

class SenialPila(SenialBase):
    pass

class SenialCola(SenialBase):
    pass

   