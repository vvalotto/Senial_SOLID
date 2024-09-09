"""
Se modifican los constructores de las clases AdquisidorConsola y AdquisidorArchivo
"""
from abc import ABCMeta, abstractmethod
from modelo.senial import *

class BaseAdquisidor(metaclass=ABCMeta):
    """
    Clase Abstracta Adquisidor
    """
    def __init__(self, senial: SenialBase):
        """
        Inicializa el adquisidor con una lista vacia de valores de la senial
        :valor: Tamanio de la coleccion de valores de la senial
        """
        self._senial = senial

    def obtener_senial_adquirida(self) -> SenialBase:
        """
        Devuelve la lista de valores de la senial adquirida
        :return: señal
        """
        return self._senial

    @abstractmethod
    def leer_senial(self) -> None:
        """
        Metodo abstracto. Cada adquisidor tiene su propia implementacion
        de la lectura de la senial
        """
        pass


class AdquisidorConsola(BaseAdquisidor):
    """
    Adquisidor de datos desde el teclado
    """
    @staticmethod
    def _leer_dato_entrada() -> float:
        """
        Lee un dato por teclaso
        :return: dato leido
        """
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, <enter>')

    def leer_senial(self) -> None:
        """
        llena la coleccion de valores de la senial desde el teclado
        """
        print("Lectura de la senial")
        for i in range(0, self._senial.tamanio):
            print(f"Dato nro: {i}")
            self._senial.poner_valor(self._leer_dato_entrada())


class AdquisidorArchivo(BaseAdquisidor):
    """
    Adquisidor de datos desde Archivo
    """

    def __init__(self, ubicacion: str):
        """
        Inicializa la instancia con la ubicación del archivo a leer
        :param ubicacion: Ubicación del archivo
        """
        super().__init__(0)
        if isinstance(ubicacion, str):
            self._ubicacion = ubicacion
        else:
            raise ValueError('El dato no es una ubicación válida, (No es un nombre de archivo)')

    @property
    def ubicacion(self) -> str:
        return self._ubicacion

    def leer_senial(self) -> None:
        print('Lectura de la senial')
        try:
            with open(self._ubicacion, 'r') as a:
                for linea in a:
                    dato = float(linea)
                    self._senial.poner_valor(dato)
                    print(dato)
        except IOError as e:
            print(f'I/O Error: {e}')
        except ValueError:
            print('Dato de señal no detectado')