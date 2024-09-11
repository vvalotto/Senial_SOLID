"""
Configura la clase que se usara
"""
from adquisidor.adquisidor import AdquisidorConsola, AdquisidorArchivo
from procesador.procesador import ProcesadorAmplificador, ProcesadorConUmbral
from visualizador.visualizador import Visualizador
from persistidor.persistidor import PersistidorPickle, PersistidorArchivo
from modelo.senial import *

def definir_senial_adquirir():
    """
    Define el tipo de estructura para la señal a adquirir
    :return:
    """
    return SenialPila(10)


def definir_senial_procesar():
    """
    Define el tipo de estructura para la señal a procesar
    :return:
    """
    return SenialPila(10)

def definir_adquisidor():
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    :return:
    """
    return AdquisidorArchivo('./adquisidor/senial.txt' ,definir_senial_adquirir())


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

def definir_persistidor(recurso):
    """
    Define el persistidor a utilizar.

    :return: Instancia de PersistidorPickle
    """
    return PersistidorArchivo(recurso)

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
    # Se configura la persitencia para los datos adquiridos
    persistidor_adquisicion = definir_persistidor('./tmp/datos/adq')
    # Se configura la persitencia para los datos procesados
    persistidor_procesamiento = definir_persistidor('./tmp/datos/pro')
