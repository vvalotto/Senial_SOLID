"""
Se modifican los constructores de las clases AdquisidorConsola y AdquisidorArchivo
"""
from abc import ABCMeta, abstractmethod
import datetime
from modelo.senial import SenialBase
from supervisor.trazador import BaseTrazador
import math


class BaseAdquisidor(BaseTrazador, metaclass=ABCMeta):
    """
    Clase Abstracta Adquisidor
    """
    def __init__(self, senial):
        """
        Inicializa el adquisidor con una lista vacía de valores de la señal
        :param senial: Instancia de SenialBase
        """
        self._senial = senial

    def obtener_senial_adquirida(self) -> SenialBase:
        """
        Devuelve la lista de valores de la senial adquirida
        :return: señal adquirida
        """
        return self._senial

    @abstractmethod
    def leer_senial(self) -> None:
        """
        Metodo abstracto. Cada adquisidor tiene su propia implementacion
        de la lectura de la senial
        """
        pass

    def trazar(self, entidad, accion, mensaje):
        """
        Registra un evento asociado a la proceso de adquisicion
        entidad: clase que genera el evento
        accion: metodo o funcion en la que se genera el evento
        mensaje: Comentario
        """
        nombre = 'adquisidor_logger.log'
        try:
            with open(nombre, 'a') as logger:
                logger.writelines('------->\n')
                logger.writelines(f'Accion: {accion}\n')
                logger.writelines(f'{entidad}\n')
                logger.writelines(f'{datetime.datetime.now()}\n')
                logger.writelines(f'{mensaje}\n')
        except IOError as eIO:
            print(f"Error al trazar la señal: {eIO}")
            raise

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

    def __init__(self, ubicacion: str, senial):
        """
        Inicializa la instancia con la ubicación del archivo a leer
        :param ubicacion: Ubicación del archivo
        """
        super().__init__(senial)
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

class AdquisidorSenoidal(BaseAdquisidor):
    """
    Simulador de una entrada de senial senoidal
    """
    def __init__(self, senial):
        """
        Inicializa el adquisidor senoidal con una señal
        :param senial: Instancia de SenialBase
        """
        BaseAdquisidor.__init__(self,senial)
        self._valor = 0.0
        self._i = 0

    def _leer_dato_entrada(self):
        """
        Genera un valor de señal senoidal
        :return: Valor de la señal senoidal
        """
        self._valor = math.sin((float(self._i) / (float(self._senial.tamanio))) * 2 * 3.14) * 10
        self._i += 1
        return self._valor

    def leer_senial(self):
        """
        Llena la colección de valores de la señal con datos senoidales
        """
        print('Lectura de la señal')
        try:
            for _ in range(self._senial.tamanio):
                self._senial.poner_valor(self._leer_dato_entrada())
        except Exception as ex:
            self.trazar(self, 'leer_senial', f'Error en la carga de datos: {ex}')
            print('Error en la carga de datos')