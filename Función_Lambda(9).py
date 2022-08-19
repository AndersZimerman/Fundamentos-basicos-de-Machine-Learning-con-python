#Función Lambda es una funciones pequeñas y anonimas (lambda)
#No es necesario proporcionar un nombre para las funciones lambda
#Se utiliza mayormente para simplificar codigo
#Sintaxis: lambda argumento1, argumento2 : expresión (cuerpo de la función)
#Ejemplo (sin lambda):
def doble(x):
    return x * 2
print(doble(200))
#Ejemplo (con lambda):
doble = lambda x: x * 2
print(doble(200))
#Ejemplo con Filter + lambda
lista = [0,1,2,3,4,5,6,7]
lista_pares = list(filter(lambda x: (x % 2 == 0),lista))
print(lista_pares)
#Ejemplo con Map + lambda
lista = [0,1,2,3,4,5,6,7]
listax2 = list(map(lambda x:x * 2,lista))
print(listax2)
#Numeros positivos
lista = [0,1,-2,3,-4,5,-6,7]
numeros_positivos = list(filter(lambda x: x > 0,lista))
print(numeros_positivos)
