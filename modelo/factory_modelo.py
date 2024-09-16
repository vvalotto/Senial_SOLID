'''
Clase Factory para Senial
'''

from modelo.senial import SenialBase, SenialLista, SenialPila, SenialCola

class FactorySenial:
    """
    Clase Factory para Senial
    """

    @staticmethod
    def fabricar_senial(tipo_senial:str, tamanio: int) -> SenialBase:
        """
        Crea una instancia de SenialBase
        :param tipo_senial: Tipo de señal a crear
        :param args: Argumentos para la creacion de la señal
        :return: Instancia de SenialBase
        """
        if tipo_senial == 'Lista':
            return SenialLista(int(tamanio))
        elif tipo_senial == 'Pila':
            return SenialPila(int(tamanio))
        elif tipo_senial == 'Cola':
            return SenialCola(int(tamanio))
        else:
            raise ValueError(f'Tipo de señal no soportado: {tipo_senial}')