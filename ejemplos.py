#Manipulación de listas:
#a. Suma de elementos de una lista:

def sumar_lista(numeros):
    suma = sum(numeros)
    return suma

lista_numeros = [1, 2, 3, 4, 5]
resultado = sumar_lista(lista_numeros)
print(resultado)  # Salida: 15
#b. Ordenar palabras alfabéticamente:

def ordenar_palabras(palabras):
    palabras_ordenadas = sorted(palabras)
    return palabras_ordenadas

lista_palabras = ['manzana', 'banana', 'kiwi', 'pera']
resultado = ordenar_palabras(lista_palabras)
print(resultado)  # Salida: ['banana', 'kiwi', 'manzana', 'pera']
#c. Elementos comunes entre dos listas:

def elementos_comunes(lista1, lista2):
    comunes = list(set(lista1) & set(lista2))
    return comunes

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
resultado = elementos_comunes(lista1, lista2)
print(resultado)  # Salida: [4, 5]
#Manejo de cadenas de texto:
#a. Contar palabras en una cadena:

def contar_palabras(cadena):
    palabras = cadena.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras

texto = "Este es un ejemplo de una cadena de texto."
resultado = contar_palabras(texto)
print(resultado)  # Salida: 8
#b. Convertir a mayúsculas:

def convertir_mayusculas(cadena):
    mayusculas = cadena.upper()
    return mayusculas

texto = "Hola, mundo!"
resultado = convertir_mayusculas(texto)
print(resultado)  # Salida: HOLA, MUNDO!
#c. Verificar si es un palíndromo:

def es_palindromo(cadena):
    cadena_sin_espacios = cadena.replace(" ", "").lower()
    inversa = cadena_sin_espacios[::-1]
    return cadena_sin_espacios == inversa

texto = "Anita lava la tina"
resultado = es_palindromo(texto)
print(resultado)  # Salida: True