"""
Configura la clase que se usará
"""

from modelo.factory_modelo import FactorySenial
from procesador.factory_procesador import FactoryProcesador
from adquisidor.factory_adquisidor import FactoryAdquisidor
from visualizador.visualizador import Visualizador
from persistidor.repositorio import RepositorioSenial
from persistidor.factory_contexto import FactoryContexto
import json
from typing import Any

# Ruta del archivo configurador.json
ruta = "./configurador/configuracion.json"

# Leer el archivo y convertirlo a diccionario
with open(ruta) as archivo:
    configurador = json.load(archivo)

def definir_senial_adquirir() -> Any:
    """
    Define el tipo de estructura para la señal a adquirir
    :return: Instancia de la señal a adquirir
    """
    senial_adq = configurador['configuracion']['senial_adq']['tipo']
    senial_adq_parametros = configurador['configuracion']['senial_adq']['tamanio']
    return FactorySenial.fabricar_senial(senial_adq, senial_adq_parametros)

def definir_senial_procesar() -> Any:
    """
    Define el tipo de estructura para la señal a procesar
    :return: Instancia de la señal a procesar
    """
    senial_pro = configurador['configuracion']['senial_pro']['tipo']
    senial_pro_parametros = configurador['configuracion']['senial_pro']['tamanio']
    return FactorySenial.fabricar_senial(senial_pro, senial_pro_parametros)

def definir_adquisidor() -> Any:
    """
    Define el adquisidor a utilizar.

    Los adquisidores disponibles son:
    - Adquisidor por Consola
    - Adquisidor por Archivo
    :return: Instancia del adquisidor
    """
    adquisidor = configurador['configuracion']['adquisidor']['tipo']
    adquisidor_parametros = configurador['configuracion']['adquisidor']['parametros']['text']
    return FactoryAdquisidor.fabricar_adquisidor(adquisidor,
                                                 definir_senial_adquirir(),
                                                 adquisidor_parametros)

def definir_procesador() -> Any:
    """
    Define el procesador a utilizar.

    Los procesadores disponibles son:
    - Procesador Amplificador
    - Procesador con Umbral
    :return: Instancia del procesador
    """
    procesador = configurador['configuracion']['procesador']['tipo']
    procesador_parametros = configurador['configuracion']['procesador']['parametros']['text']
    return FactoryProcesador.fabricar_procesador(procesador,
                                                 definir_senial_procesar(),
                                                 procesador_parametros)

def definir_visualizador() -> Visualizador:
    """
    Define el visualizador a utilizar.
    :return: Instancia de Visualizador
    """
    return Visualizador()

def definir_contexto(recurso: str) -> Any:
    """
    Define el contexto a utilizar.

    Los contextos disponibles son:
    - Almacenar en archivos txt
    - Almacenar en archivos pickle
    :param recurso: Recurso a utilizar
    :return: Instancia del contexto
    """
    contexto = configurador['configuracion']['contexto']
    return FactoryContexto.fabricar_contexto(contexto, recurso)

def definir_repositorio(contexto: Any) -> RepositorioSenial:
    """
    Define el repositorio a utilizar.
    :param contexto: Contexto a utilizar
    :return: Instancia del repositorio
    """
    return RepositorioSenial(contexto)

class Configurador:
    """
    El Configurador es un contenedor de objetos que participan de la solución
    """
    senial_adquirir = definir_senial_adquirir()
    senial_procesar = definir_senial_procesar()

    # Configura los contextos de datos
    ctx_datos_adquisicion = definir_contexto('./tmp/datos/adq')
    ctx_datos_procesamiento = definir_contexto('./tmp/datos/pro')

    # Configura los repositorios de las entidades a usar
    rep_adquisicion = definir_repositorio(ctx_datos_adquisicion)
    rep_procesamiento = definir_repositorio(ctx_datos_procesamiento)

    # Configura los adquisidores, procesadores y visualizadores
    # Se configura el tipo de adquisidor
    adquisidor = definir_adquisidor()
    # Se configura el tipo de procesador
    procesador = definir_procesador()
    # Se configura el visualizador
    visualizador = definir_visualizador()
