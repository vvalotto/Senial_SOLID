"""
Configura la clase que se usara
"""
from adquisidor.adquisidor import AdquisidorConsola, AdquisidorArchivo
from procesador.procesador import ProcesadorAmplificador, ProcesadorConUmbral
from visualizador.visualizador import Visualizador
from modelo.senial import Senial,SenialPila, SenialCola

def definir_senial_adquirir():
    """
    Define el tipo de estructura para la señal a adquirir
    :return:
    """
    return Senial(5)


def definir_senial_procesar():
    """
    Define el tipo de estructura para la señal a procesar
    :return:
    """
    return SenialPila(5)

def definir_adquisidor():
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    :return:
    """
    return AdquisidorConsola(definir_senial_adquirir())


def definir_procesador():
    """
    Los procesadores son:
    Procesador Amplificador
    Procesador con Umbral

    """
    return ProcesadorAmplificador(definir_senial_procesar(),2)

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
