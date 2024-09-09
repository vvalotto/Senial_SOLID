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
        self._valores: List = []
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
    def poner_valor(self, valor: float) -> None:
        """
        Agrega un valor al final de la lista de la señal.
        :param valor: Dato de la señal obtenida.
        """
        if self._cantidad >= self._tamanio:
            print('Error: No se pueden poner más datos')
            return
        self._valores.append(valor)
        self._cantidad += 1

    def sacar_valor(self, indice: int) -> Any:
        """
        Saca un valor en una posición cualquiera de la lista de la señal.
        :param indice: Índice del valor a sacar.
        :return: Valor sacado de la lista.
        """
        if self._cantidad == 0:
            print('Error: No hay valores para sacar')
            return None
        try:
            valor = self._valores.pop(indice)
            self._cantidad -= 1
            return valor
        except IndexError:
            print(f'Error: Índice {indice} fuera de rango')
            return None

class SenialPila(SenialBase):
    def poner_valor(self, valor: float) -> None:
        """
        Agrega un valor al final de la pila de la señal.
        :param valor: Dato de la señal obtenida.
        """
        if self._cantidad >= self._tamanio:
            print('Error: No se pueden poner más datos')
            return
        self._valores.append(valor)
        self._cantidad += 1

    def sacar_valor(self) -> Any:
        """
        Saca un valor del final de la pila de la señal.
        :return: Valor sacado de la pila.
        """
        if self._cantidad == 0:
            print('Error: No hay valores para sacar')
            return None
        self._cantidad -= 1
        return self._valores.pop()

class SenialCola(SenialBase):
    def __init__(self, tamanio: int):
        """
        Construye la instancia de la estructura cola circular, donde se indica el
        tamaño de la cola y se inicializan los punteros de la cabeza y cola.
        :param tamanio: Tamaño de la cola.
        """
        super().__init__(tamanio)
        self._cabeza: int = 0
        self._cola: int = 0
        self._valores: List[Any] = [None] * tamanio

    def poner_valor(self, valor: float) -> None:
        """
        Agrega un valor al final de la cola de la señal.
        :param valor: Dato de la señal obtenida.
        """
        if self._cantidad >= self._tamanio:
            print('Error: No se pueden poner más datos')
            return
        self._valores[self._cola] = valor
        self._cola = (self._cola + 1) % self._tamanio
        self._cantidad += 1

    def sacar_valor(self) -> Any:
        """
        Saca un valor del inicio de la cola de la señal.
        :return: Valor sacado de la cola.
        """
        if self._cantidad == 0:
            print('Error: No hay valores para sacar')
            return None
        valor = self._valores[self._cabeza]
        self._valores[self._cabeza] = None
        self._cabeza = (self._cabeza + 1) % self._tamanio
        self._cantidad -= 1
        return valor

   