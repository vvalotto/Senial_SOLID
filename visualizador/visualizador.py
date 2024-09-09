"""
Clase que genera la salida y visualizacion del contenido de la señal
"""
from modelo.senial import *


class Visualizador:

    def mostrar_datos(self, senial: SenialBase) -> None:
        """
        Muestra los datos de la señal
        :param senial: Señal a mostrar
        """
        print('Mostrar la senial')
        for i in range(0, senial.obtener_tamanio()):
            print(senial.sacar_valor())
