"""
Configura la clase que se usara
"""
from adquisidor.adquisidor import AdquisidorConsola, AdquisidorArchivo
from procesador.procesador import ProcesadorAmplificador, ProcesadorConUmbral
from visualizador.visualizador import Visualizador

def definir_adquisidor():
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    :return:
    """
    return AdquisidorArchivo('./adquisidor/senial.txt')


def definir_procesador():
    """
    Los procesadores son:
    Procesador Amplificador
    Procesador con Umbral

    """
    return ProcesadorAmplificador(2)

def definir_visualizador():
    """
    Define el visualizador a utilizar.

    :return: Instancia de Visualizador
    """
    return Visualizador()

class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()
