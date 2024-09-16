"""
Fabrica de adquisidores
"""

from adquisidor.adquisidor import *
from modelo.senial import SenialBase
from typing import Any

class FactoryAdquisidor:
    """
    Clase que fabrica adquisidores.
    """

    @staticmethod
    def fabricar_adquisidor(tipo_adquisidor: str, senial: SenialBase, parametros: Any) -> BaseAdquisidor:
        """
        Fabrica un adquisidor.
        :param tipo_adquisidor: Tipo de adquisidor.
        :param senial: Señal a adquirir.
        :return: Adquisidor
        """
        if tipo_adquisidor == 'Simple':
            return AdquisidorConsola(senial)
        elif tipo_adquisidor == 'Archivo':
            return AdquisidorArchivo(str(parametros), senial)
        elif tipo_adquisidor == 'Senoidal':
            return AdquisidorSenoidal(senial)
        else:
            raise ValueError('Adquisidor no soportado')