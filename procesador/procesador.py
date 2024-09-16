"""
Se modifica el archivo procesador.py para que las clases
ProcesadorAmplificador y ProcesadorConUmbral hereden de BaseProcesador
"""

from abc import ABCMeta, abstractmethod
from modelo.senial import *


class BaseProcesador(metaclass=ABCMeta):
    """
    Clase Abstracta Procesador
    """
    def __init__(self, senial: SenialBase):
        """
        Se inicializa con la senial que se va a procesar
        """
        self._senial_procesada = senial
        return

    @abstractmethod
    def procesar(self, senial) -> None:
        """
        Metodo abstracto que se implementara para cada tipo de procesamiento
        """
        pass

    def obtener_senial_procesada(self) -> SenialBase:
        """
        Devuelve la señal procesada
        """
        return self._senial_procesada


class ProcesadorAmplificador(BaseProcesador):
    """
    Clase Procesador Amplificador
    """
    def __init__(self, senial: SenialBase, amplificacion: float):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el valor de amplificacion
        :param amplificacion: Valor de amplificación
        """
        super().__init__(senial)
        self._amplificacion = amplificacion

    def procesar(self, senial) -> None:
        """
        Implementa el procesamiento de amplificar cada valor de senial
        :param senial: Señal a procesar
        """
        print("Procesando...")
        self._senial_procesada.poner_valores(list(map(self._amplificar, senial.obtener_valores())))
        self._senial_procesada.cantidad += len(self._senial_procesada.valores)

    def _amplificar(self, valor) -> float:
        """
        Función que retorna el valor amplificado
        :param valor: Valor de entrada
        :return: Valor amplificado
        """
        return valor * self._amplificacion


class ProcesadorConUmbral(BaseProcesador):
    """
    Clase Procesador con Umbral
    """
    def __init__(self, senial: SenialBase, umbral: float):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el umbral
        :param umbral: Valor del umbral
        """
        super().__init__(senial)
        self._umbral = umbral

    def procesar(self, senial) -> None:
        """
        Implementa el procesamiento de la señal con umbral
        :param senial: Señal a procesar
        """
        print("Procesando con umbral")
        self._senial_procesada.poner_valores(list(map(self._funcion_umbral, senial.obtener_valores())))
        self._senial_procesada.cantidad += len(self._senial_procesada.valores)

    def _funcion_umbral(self, valor) -> float:
        """
        Función que filtra valores con un umbral
        :param valor: Valor de entrada
        :return: Valor filtrado
        """
        return valor if valor < self._umbral else 0