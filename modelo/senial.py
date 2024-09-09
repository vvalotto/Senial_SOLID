"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio
Modificacion: Se agregan miembros de instancias y se definen como propiedades
"""
from typing import Any, List


class Senial:

    def __init__(self, tamanio: int = 10):
        """
        Constructor: Inicializa la lista de valores vacía.
        :param tamanio: Tamaño inicial de la señal.
        """
        self._valores: List[float] = []
        self._fecha_adquisicion = None
        self._cantidad = 0
        self._tamanio = tamanio

    # Propiedades
    @property
    def fecha_adquisicion(self) -> Any:
        return self._fecha_adquisicion

    @fecha_adquisicion.setter
    def fecha_adquisicion(self, valor) -> None:
        self._fecha_adquisicion = valor

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor) -> None:
        self._cantidad = valor

    @property
    def tamanio(self) -> int:
        return self._tamanio

    @tamanio.setter
    def tamanio(self, valor)-> None:
        self._tamanio = valor

    @property
    def valores(self) -> List[float]:
        return self._valores

    @valores.setter
    def valores(self, datos: List[float]) -> None:
        self._valores = datos

    def poner_valor(self, valor: float) -> None:
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self._valores.append(valor)

    def obtener_valor(self, indice: int) -> Any:
        """
        Recupera el contenido según el indice
        :param indice: Indice del valor a recuperar.
        :return: Valor en el indice especificado.
        """
        try:
            valor = self._valores[indice]
            return valor
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