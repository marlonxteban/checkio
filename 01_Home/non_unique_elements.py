"""
Se te dará una lista no vacía de enteros (X). Para esta misión, deberás retornar una lista que consista únicamente de elementos no únicos. Para hacerlo, necesitarás remover todos los ementos que sean únicos (elementos que aparezcan una sola vez en la lista dada). Al resolver esta misión, no cambies el orden de la lista. Ejemplo: [1, 2, 3, 1, 3] 1 y 3 no son elementos únicos y el resultado será [1, 3, 1, 3].
non-unique-elements
Entrada: Una lista de enteros.
Salida: Otra lista de enteros.
¿Cómo es usado?: Esta misión te ayudará a entender cómo manipular vectores (arrays), que es la base para resolver tareas más complejas. El concepto puede ser fácilmente generalizado para tareas en el mundo real. Por ejemplo: si necesitas esclarecer estadísticas removiendo elementos de baja frecuencia (ruido).
Pre-condición:
0 < |X| < 1000
"""

def checkio(data):
    doble = list()
    for x in data:
        if data.count(x) >=2:
            doble.append(x)      
    return doble