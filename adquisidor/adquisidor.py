"""
Para OCP
Se refactoriza la clase de manera de extender otros tipos de
funciones de adquisicion de datos sin que impacte en los anteriores programas
o que cambiando solo las clases de alto nivel que puedan "armar" la solucion
"""
from abc import ABCMeta, abstractmethod
from modelo.senial import Senial


class BaseAdquisidor(metaclass=ABCMeta):
    """
    Clase Abstracta Adquisidor
    """
    def __init__(self, valor):
        """
        Inicializa el adquisidor con una lista vacia de valores de la senial
        :valor: Tamanio de la coleccion de valores de la senial
        """
        self._senial = Senial()
        self._nro_muestra = valor

    def obtener_senial_adquirida(self):
        """
        Devuelve la lista de valores de la senial adquirida
        :return: señal
        """
        return self._senial

    @abstractmethod
    def leer_senial(self):
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
    def _leer_dato_entrada():
        """
        Lee un dato por teclaso
        :return: dato leido
        """
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, <enter>')

    def leer_senial(self):
        """
        llena la coleccion de valores de la senial desde el teclado
        """
        print("Lectura de la senial")
        for i in range(0, self._nro_muestra):
            print(f"Dato nro: {i}")
            self._senial.poner_valor(self._leer_dato_entrada())


class AdquisidorArchivo(BaseAdquisidor):
    """
    Adquisidor de datos desde Archivo
    """

    def __init__(self, ubicacion):
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
    def ubicacion(self):
        return self._ubicacion

    def leer_senial(self):
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