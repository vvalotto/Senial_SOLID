"""
Clase que genera la salida y visualizacion del contenido de la señal
"""
from modelo.senial import Senial

class Visualizador:

    def mostrar_datos(self, senial: Senial) -> None:
        """
        Muestra los datos de la señal
        :param senial: Señal a mostrar
        """
        print('Mostrar la senial')
        for i in range(0, senial.obtener_tamanio()):
            print(senial.obtener_valor(i))
