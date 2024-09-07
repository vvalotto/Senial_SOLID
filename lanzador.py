__author__ = 'Victor Valotto'
__version__ = '0.0.1'
__date__ = '2021/09/01'
__author_email__ = 'vvalotto@gmail.com'

"""
Programa lanzador del ejemplo
"""

from senial_solid.lector_senial import LectorSenial


class Lanzador:
    """
    Programa Principal
    """

    def __init__(self):
        pass

    @staticmethod
    def ejecutar() -> None:
        """
        Ejecucion del programa lanzador
        """
        senial = LectorSenial(10)

        print("Iniciando")
        print("Paso 1 - Adquiere la señal")
        senial.leer_senial()

        print("Paso 2 - Procesa la señal")
        senial.procesar_senial()

        print("Paso 3 - Muestra la señal")
        senial.mostrar_senial()


if __name__ == "__main__":
    Lanzador().ejecutar()
