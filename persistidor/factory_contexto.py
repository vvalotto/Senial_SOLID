'''
Clase Factory para Contexto
'''

from persistidor.contexto import ContextoArchivo, ContextoPickle, BaseContexto

class FactoryContexto:
    """
    Clase Factory para Contexto
    """

    @staticmethod
    def fabricar_contexto(tipo_contexto:str, recurso: str) -> BaseContexto:
        """
        Crea una instancia de ContextoBase
        :param tipo_contexto: Tipo de contexto a crear
        :param recurso: Recurso a utilizar
        :return: Instancia de ContextoBase
        """
        if tipo_contexto == 'archivo':
            return ContextoArchivo(recurso)
        elif tipo_contexto == 'pickle':
            return ContextoPickle(recurso)
        else:
            raise ValueError(f'Tipo de contexto no soportado: {tipo_contexto}')