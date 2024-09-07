"""
Ejemplo de violación del principio de SRP
Aqui la clase LectorSenial tiene todas las responsabilidades del
procesamiento de una senial
"""


class LectorSenial:
    """
    Clase que posee todas las fases del procesamiento de una señal:
    1. Lectura de la señal
    2. Procesamiento
    3. Visualización de la señal procesada
    """

    def __init__(self, tamanio: int):
        """
        Inicializa la instancia del lector.
        Inicializa la lista de datos a obtener.
        Inicializa la lista de datos a procesar.
        :param tamanio: número de valores de la señal a procesar
        """
        self._nro_muestra = tamanio
        self._valores = []
        self._valores_procesados = []

    def __leer_dato_entrada(self) -> float:
        """
        Metodo privado que se usa para ingresar un solo valor.
        En este caso se ingresa por consola.
        """
        while True:
            try:
                return float(input('Valor: '))
            except ValueError:
                print('Dato mal ingresado, <enter>')

    def leer_senial(self) -> None:
        """
        Obtiene la señal de entrada y la guarda en la lista interna.
        """
        print("Lectura de la señal")
        for i in range(self._nro_muestra):
            print(f"Dato nro: {i}")
            self._valores.append(self.__leer_dato_entrada())

    def procesar_senial(self) -> None:
        """
        Procesa la señal de manera que para cada valor adquirido se
        obtenga el doble del mismo.
        """
        print("Procesando Señal")
        self._valores_procesados = [valor * 2 for valor in self._valores]

    def mostrar_senial(self) -> None:
        """
        Muestra la señal procesada en salida de consola.
        """
        print("Mostrar la señal")
        for valor in self._valores_procesados:
            print(valor)
