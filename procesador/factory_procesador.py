'''
Clase Factory para Procesador
'''

from procesador.procesador import ProcesadorAmplificador, ProcesadorConUmbral, BaseProcesador
from modelo.senial import SenialBase
from typing import Any

class FactoryProcesador:
    """
    Clase Factory para Procesador
    """

    @staticmethod
    def fabricar_procesador(tipo_procesador:str, senial: SenialBase, parametros: Any) -> BaseProcesador:
        """
        Crea una instancia de ProcesadorBase
        :param tipo_procesador: Tipo de procesador a crear
        :param senial: Señal a procesar
        :param umbral: Umbral a utilizar
        :return: Instancia de ProcesadorBase
        """
        if tipo_procesador == 'Amplificador':
            return ProcesadorAmplificador(senial, int(parametros))
        elif tipo_procesador == 'Umbral':
            return ProcesadorConUmbral(senial, int(parametros))
        else:
            raise ValueError(f'Tipo de procesador no soportado: {tipo_procesador}')