__author__ = 'Victor Valotto'
__version__ = '2.0.0'
__date__ = '2021/09/01'
__author_email__ = 'vvalotto@gmail.com'

"""
Ejemplo de solucion para el SRP, donde las responsabilidades se dividen
entre diferentes clases separadas en diferentes módulos a implementar.
"""
import os
from adquisidor.adquisidor import Adquisidor
from procesador.procesador import Procesador
from visualizador.visualizador import Visualizador
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
    def seleccionar_procesador():
        """
        Pide al usuario la seleccion del tipo de procesador
        """
        os.system("clear")
        print("Seleccionar tipo de procesamiento:")
        print("1 > Valor Doble")
        print("2 > Umbral")
        while True:
            op = input('Opcion: ')
            if op in ['1', '2']:
                break
        return op

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
    def ejecutar()->None:
        """
        Se instancian las clases que participan del procesamiento
        """
        Lanzador.informar_versiones()
        Lanzador.tecla()
        opcion = Lanzador.seleccionar_procesador()

        # Se instancian las clases que participan del procesamiento
        mi_adquisidor = Adquisidor(5)
        if opcion == '1':
            # Si es para amplificar pasa el valor a amplificar
            mi_procesador = Procesador(2)
        elif opcion == '2':
            # Si es umbral pasa el valor de umbral
            mi_procesador = Procesador(5)
        else:
            mi_procesador = None

        os.system("clear")
        print("Incio - Paso 1 - Adquisicion de la senial")
        # Paso 1 - Se obtiene la senial
        mi_adquisidor.adquirir_senial()
        senial_adquirida = mi_adquisidor.obtener_senial_adquirida()
        Lanzador.tecla()
        os.system("clear")

        # Paso 2 - Se procesa la senial adquirida
        print("Incio - Paso 2 - Procesamiento")

        try:
            if opcion == '1':
                mi_procesador.procesar_senial(senial_adquirida)
            elif opcion == '2':
                mi_procesador.procesar_senial_con_umbral(senial_adquirida)
            else:
                print('Sin procesador selecionado')
                print("Fin Programa - NoOCP")
                exit()
        except Exception():
            print("Error al procesar")
            print("Fin Programa - NoOCP")
            exit()

        senial_procesada = mi_procesador.obtener_senial_procesada()
        Lanzador.tecla()
        os.system("clear")

        # Paso 3 - Se muestran las seniales
        print("Incio - Paso 3 - Mostrar Senial")
        Visualizador().mostrar_datos(senial_procesada)
        print("Fin Programa - NoOCP")


if __name__ == "__main__":
    Lanzador().ejecutar()