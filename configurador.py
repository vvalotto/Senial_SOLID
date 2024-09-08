"""
Configura la clase que se usará.
"""

from procesador.procesador import ProcesadorAmplificador, ProcesadorConUmbral


def definir_procesador():
    """
    Define el procesador a utilizar.

    Los procesadores disponibles son:
    - Procesador Amplificador
    - Procesador con Umbral

    :return: Instancia de ProcesadorAmplificador
    """
    return ProcesadorConUmbral(4)


class Configurador:
    """
    El Configurador es un contenedor de objetos que participan de la solución.
    """

    # Se configura el tipo de procesador
    procesador = definir_procesador()
