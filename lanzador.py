__author__ = 'Victor Valotto'
__version__ = '4.0.0'
__date__ = '2021/09/01'
__author_email__ = 'vvalotto@gmail.com'

"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases separadas en diferentes módulos a implementar.
"""
import os
from configurador import Configurador
import adquisidor
import procesador
import visualizador
import modelo


class Lanzador:
    """
    Programa Lanzador
    """


    @staticmethod
    def tecla()->None:
        """
        Funcion que solicita un tecla para continuar
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
        print("Versiones de los componenetes")
        print("adquisidor: " + adquisidor.__version__)
        print("procesador: " + procesador.__version__)
        print("visualizador: " + visualizador.__version__)
        print("modelo: " + modelo.__version__)

    @staticmethod
    def ejecutar() -> None:
        # Se instancian las clases que participan del procesamiento
        Lanzador.informar_versiones()
        Lanzador.tecla()

        # Se instancian las clases que participan del procesamiento
        mi_adquisidor = Configurador.adquisidor
        mi_procesador = Configurador.procesador
        mi_visualizador = Configurador.visualizador

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        '''Paso 1 - Se obtiene la senial'''
        mi_adquisidor.leer_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()

        '''Paso 2 - Se procesa la senial adquirida'''
        print("Incio - Paso 2 - Procesamiento")
        mi_procesador.procesar(senial_adquirida)
        senial_procesada = mi_procesador.obtener_senial_procesada()
        Lanzador.tecla()

        '''Paso 3 - Se muestran las seniales '''
        print("Incio - Paso 3 - Mostrar Senial")
        mi_visualizador.mostrar_datos(senial_procesada)
        print("Fin Programa")



if __name__ == "__main__":
    Lanzador().ejecutar()