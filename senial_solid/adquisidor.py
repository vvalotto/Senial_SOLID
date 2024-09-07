"""
Modulo que define la clase Adquisidor
"""
from senial_solid.senial import Senial


class Adquisidor():
    """
        Clase que adquiere la señal
        """

    def __init__(self, tamanio: int):
        self._nro_muestra = tamanio
        self._senial = Senial()

    def __leer_dato_entrada(self) -> float:
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, <enter>')

    def adquirir_senial(self) -> Senial:
        print("Adquiriendo la señal")
        for i in range(self._nro_muestra):
            print(f"Dato nro: {i}")
            self._senial.poner_valor(self.__leer_dato_entrada())
        return self._senial

    def obtener_senial_adquirida(self) -> Senial:
        """
        Devuelva la señal con valores
        """
        return self._senial