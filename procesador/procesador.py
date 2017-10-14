"""
Define la clase procesador de la senial
Cambio 1:
Uso de la funcion map para calcular valores de la lista
"""
from modelo.senial import *


class Procesador(object):
    """
    Constructor: Inicializa la clase
    """
    def __init__(self):
        self._senial_procesada = Senial()
        return
    
    def procesar_senial(self, senial):
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        :return:
        """
        print("Procesando...")
        self._senial_procesada._valores = list(map(self.funcion_doble, senial._valores))
        return
    
    def obtener_senial_procesada(self):
        """
        Devuelve la senial procesada
        :return:
        """
        return self._senial_procesada

    @staticmethod
    def funcion_doble(valor):
        """
        Funcion que retorna el doble de valor de entrada
        :param valor:
        :return:
        """
        return valor * 2
