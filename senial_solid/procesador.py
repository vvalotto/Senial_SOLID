"""
Define la clase procesador de la senial
"""
from senial_solid.senial import Senial


class Procesador:
    """
    Constructor: Inicializa la senial que resultara procesada.
    """

    def __init__(self):
        self._senial_procesada = Senial()

    def procesar_senial(self, senial) -> None:
        """
        Metodo que realiza el procesamiento de la senial
        :param senial: a procesar
        """
        print("Procesando...")
        for i in range(0, senial.obtener_tamanio()):
            self._senial_procesada.poner_valor(senial.obtener_valor(i) * 2)

    def obtener_senial_procesada(self) -> Senial:
        """
        Devuelve la senial procesada
        :return: Senial procesada
        """
        return self._senial_procesada