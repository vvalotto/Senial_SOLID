"""
Modulo que define la entidad Senial.
Es considerada una entidad del dominio
"""
from typing import Any


class Senial:
    """
    Definicion de la entidad tipo Senial.
    En este caso es una definicion de una clase concreta.
    Tiene las funciones:
    -> poner_valor(valor)
    -> obtener_valor(indice)
    -> obtener_tamanio()
    """

    def __init__(self):
        """
        Constructor: Inicializa la lista de valores vacia
        """
        self._valores = []

    def poner_valor(self, valor: float) -> None:
        """
        Agrega dato a la lista de la senial
        :param valor: dato de la senial obtenida
        """
        self._valores.append(valor)

    def obtener_valor(self, indice: int) -> Any:
        """
        Recupera el contenido según el indice
        :param indice: Indice del valor a recuperar.
        :return: Valor en el indice especificado.
        """
        try:
            valor = self._valores[indice]
            return valor
        except Exception as ex:
            print('Error: ', ex.args)
            return None

    def obtener_tamanio(self) -> int:
        """
        Retorna el largo de la lista de valores.
        :return: Tamaño de la lista de valores.
        """
        return len(self._valores)

    def obtener_valores(self) -> list:
        """
        Retorna la lista de valores.
        :return: Lista de valores.
        """
        return self._valores

    def poner_valores(self, valores: list) -> None:
        """
        Agrega una lista de valores a la lista de la señal
        :param valores: lista de valores a agregar
        """
        self._valores = valores