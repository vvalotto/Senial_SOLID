"""
Configura la clase que se usará.
"""

from procesador.procesador import *
from adquisidor.adquisidor import *
from visualizador.visualizador import *

def definir_adquisidor():
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    """
    return AdquisidorArchivo('./adquisidor/datos.txt')

def definir_procesador():
    """
    Define el procesador a utilizar.

    Los procesadores disponibles son:
    - Procesador Amplificador
    - Procesador con Umbral
    """
    return ProcesadorConUmbral(20)

def definir_visualizador():
    return Visualizador()


class Configurador:
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()
