"""
Para OCP
Se refactoriza la clase de manera de extender otros tipos de
funciones de procesmiento de datos sin que impacte en los anteriores programas
o que cambiando solo las clases de alto nivel que pueda "armar" la solucion
"""
from abc import ABCMeta, abstractmethod
from modelo.senial import Senial


class BaseProcesador(metaclass=ABCMeta):
    """
    Clase Abstracta Procesador
    """
    def __init__(self):
        """
        Se inicializa con la senial que se va a procesar
        """
        self._senial_procesada = Senial()
        return

    @abstractmethod
    def procesar(self, senial):
        """
        Metodo abstracto que se implementara para cada tipo de procesamiento
        """
        pass

    def obtener_senial_procesada(self):
        """
        Devuelve la señal procesada
        """
        return self._senial_procesada


class ProcesadorAmplificador(BaseProcesador):
    """
    Clase Procesador Amplificador
    """
    def __init__(self, amplificacion):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el valor de amplificacion
        :param amplificacion: Valor de amplificación
        """
        super().__init__()
        self._amplificacion = amplificacion

    def procesar(self, senial):
        """
        Implementa el procesamiento de amplificar cada valor de senial
        :param senial: Señal a procesar
        """
        print("Procesando...")
        self._senial_procesada.poner_valores(list(map(self._amplificar, senial.obtener_valores())))

    def _amplificar(self, valor):
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
    def __init__(self, umbral):
        """
        Sobreescribe el constructor de la clase abstracta para inicializar el umbral
        :param umbral: Valor del umbral
        """
        super().__init__()
        self._umbral = umbral

    def procesar(self, senial):
        """
        Implementa el procesamiento de la señal con umbral
        :param senial: Señal a procesar
        """
        print("Procesando con umbral")
        self._senial_procesada.poner_valores(list(map(self._funcion_umbral, senial.obtener_valores())))

    def _funcion_umbral(self, valor):
        """
        Función que filtra valores con un umbral
        :param valor: Valor de entrada
        :return: Valor filtrado
        """
        return valor if valor < self._umbral else 0