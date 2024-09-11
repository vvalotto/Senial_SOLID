__author__ = 'Victor Valotto'
__version__ = '7.0.0'
__date__ = '2021/09/01'
__author_email__ = 'vvalotto@gmail.com'

from modelo.senial import SenialBase

"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases separadas en diferentes módulos a implementar.
"""
import os
import adquisidor
import procesador
import visualizador
import persistidor
import modelo
from configurador import Configurador, definir_senial_adquirir, definir_senial_procesar
from datetime import datetime

class Lanzador:
    """
    Programa Lanzador
    """

    @staticmethod
    def tecla() -> None:
        """
        Funcion que solicita una tecla para continuar
        """
        while True:
            if input('C para continuar> ') == "C":
                break
        os.system("clear")

    @staticmethod
    def informar_versiones() -> None:
        """
        Informa las versiones de los componentes
        """
        os.system("clear")
        print("Versiones de los componentes")
        print(f"adquisidor: {adquisidor.__version__}")
        print(f"procesador: {procesador.__version__}")
        print(f"visualizador: {visualizador.__version__}")
        print(f"persistidor: {persistidor.__version__}")
        print(f"modelo: {modelo.__version__}")

    @staticmethod
    def ejecutar() -> None:
        """
        Programa principal
        """
        # Se prepara el programa
        Lanzador.informar_versiones()
        Lanzador.tecla()

        # Se instancian las clases que participan del procesamiento
        mi_adquisidor = Configurador.adquisidor
        mi_procesador = Configurador.procesador
        mi_visualizador = Configurador.visualizador
        persistidor_adquisicion = Configurador.persistidor_adquisicion
        persistidor_procesamiento = Configurador.persistidor_procesamiento

        os.system("clear")
        print("Inicio - Paso 1 - Adquisicion de la senial")
        # Paso 1 - Se obtiene la senial
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        senial_adquirida.fecha_adquisicion = datetime.now().date()
        senial_adquirida.comentario = input('Descripcion de la señal:')
        senial_adquirida.id = int(input('Identificacion (nro entero)'))
        print('Fecha de lectura: {0}'.format(senial_adquirida.fecha_adquisicion))
        print('Cantidad de valores obtenidos {0}'.format(senial_adquirida.cantidad))

        Lanzador.tecla()
        print('Se persiste la señal adquirida')
        persistidor_adquisicion.persistir(senial_adquirida, str(senial_adquirida.id))
        print('Señal Guardada')

        # Paso 2 - Se procesa la senial adquirida
        print("Inicio - Paso 2 - Procesamiento")
        mi_procesador.procesar(senial_adquirida)
        senial_procesada = mi_procesador.obtener_senial_procesada()

        Lanzador.tecla()
        print('Se persiste la señal procesada')
        senial_procesada.comentario = input('Descripción de la señal procesada:')
        senial_procesada.id = int(input('Identificación (nro entero): '))
        persistidor_procesamiento.persistir(senial_procesada, str(senial_procesada.id))
        print('Señal Procesada Guardada')

        # Paso 3 - Se muestran las seniales
        print("Inicio - Paso 3 - Mostrar Señales")
        adquirida = persistidor_adquisicion.recuperar(definir_senial_adquirir(), senial_adquirida.id)
        print('Señal adquirida----->')
        mi_visualizador.mostrar_datos(adquirida)
        procesada = persistidor_procesamiento.recuperar(definir_senial_procesar(), senial_procesada.id)
        print('Señal procesada----->')
        mi_visualizador.mostrar_datos(procesada)

if __name__ == "__main__":
    Lanzador().ejecutar()