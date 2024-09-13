"""
Configura la clase que se usara
"""
from adquisidor.adquisidor import *
from procesador.procesador import *
from visualizador.visualizador import Visualizador
from persistidor.contexto import *
from persistidor.repositorio import RepositorioSenial
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
    return SenialLista(10)

def definir_adquisidor():
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    :return:
    """
    return AdquisidorSenoidal(definir_senial_adquirir())



def definir_procesador():
    """
    Los procesadores son:
    Procesador Amplificador
    Procesador con Umbral

    """
    return ProcesadorAmplificador(definir_senial_procesar(),10)

def definir_visualizador():
    """
    Define el visualizador a utilizar.

    :return: Instancia de Visualizador
    """
    return Visualizador()

def definir_contexto(recurso):
    """
    Los contexto son:
    Almancenar en archivos txt
    Almacenar en archivos pickle
    :param recurso:
    :return:
    """
    return ContextoArchivo(recurso)

def definir_repositorio(contexto):
    return RepositorioSenial(contexto)

class Configurador(object):
    """
    El Configurador es un contenedor de objetos que participan de la solucion
    """
    #Configura los contextos de datos
    ctx_datos_adquisicion = definir_contexto('./tmp/datos/adq')
    ctx_datos_procesamiento = definir_contexto('./tmp/datos/pro')

    #Configura los repositorios de las entidades a usar
    rep_adquisicion = definir_repositorio(ctx_datos_adquisicion)
    rep_procesamiento = definir_repositorio(ctx_datos_procesamiento)

    # Configura los adquisidores, procesadores y visualizadores
    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()

