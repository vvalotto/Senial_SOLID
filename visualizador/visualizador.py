"""
Clase que genera la salida y visualizacion del contenido de la señal
"""


class Visualizador(object):

    @staticmethod
    def mostrar_datos(senial):
        print('Mostrar la senial')
        for i in range(0, senial.tamanio):
            print(senial.obtener_valor(i))
        return
