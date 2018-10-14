# Senial_SOLID
Demostración de la aplicación de los Principios de Diseño SOLID

S -> SRP: Principio de Responsabiidad Única
O -> OCP: Principio de Abierto/Cerrado
L -> LSP: Principio de Sustitución de Liskov
I -> SIP: Principio de Segregación de Interfases
D -> DIP: Principio de Inversión de Dependencias

Requerimiento 1:

Se desea que se simule el ingreso de una señal por consola, donde cada valor es ingresado por es
método. La lista de valores ingresado (la sañal) debe ser procesada mediante generando una nueva
señal amplificada al doble de la ingresa y posteriormente mostrar el resultado de la señal
amplificada.

Requerimiento 2:

Es necesario agregar un nuevo tipo de procesamiento ya que hay clientes que necesitan valores de
la señal por debajo de un umbral de valores, que son entregados en un archivo.
Es una nueva versión del Senial_SOLID, pero mantiene la funcionalidad existente.

Requerimiento 3:

Los valores que corresponden a la señal son manejado como una lista, los desarrolladore están viendo
que agregar el manejo de la colección de valores de la señal también como una pila y una cola, además
de una lista.

Requerimiento 4:

Las datos adquiridos y procesados deben ser guardados.