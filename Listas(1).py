#una lista:
#no te olvides de las comas
lista = [['hola mundo'],1,2,4,'a','b','python',4.5]
print(lista)
#ahora veremos una lista (suma)
lista_a = [1,2,3,4]
lista_b = [5,6,7,8]
suma = lista_a + lista_b
print(suma)
#no sumamaos literal solo agrgamos el conjunto (lo unimos) algo así:
lista_a = ['a','b','c','d']
lista_b = [5,6,7,8]
suma = lista_a + lista_b
print(suma)
#remplasaremos valores (numericos) 
#antes
numeros = [1,2,3,4,5]
print(numeros)
#despues
numeros = [1,2,3,4,5]
numeros [1] = 9
print(numeros)
#tambien sirve para texto o valers flotantes
numeros = [1,2,3,4,5]
numeros [1] = "nuevo"
numeros [4] = 4.5
print(numeros)
#para ve cuantos numeros tenemos en una lista usamoas (len) len no suenta desde cero 
lista = [1,2,3,4]
print(len(lista))
#me marca 4 en conteo 
#solo toma en cuena desde la posicion 1 y como no especificamos hasta,
#que posicion asimilara hasta la ultima pocisión
lista = [1,2,3,4,5]
print(lista[1:])
#lo mismo pasa al reves
lista = [1,2,3,4,5]
print(lista[:4])
#cojer solo un conjunto
lista = [1,2,3,4,5]
print(lista[1:4])
#con un indice mas al final de lista []:
lista = [1,2,3,4,5]
print(lista[1:4:2])
#agragar valores
lista = [1,2,3,4,5,6,7]
lista2 = ['a','b','c']
lista.extend(lista2)
print(lista)
#ordenar letros o numeros .sort()
letras = ['xyz','abc','mno']
letras.sort()
print(letras)
#numeros
numeros = [5,3,7,8,2,1,4,6]
numeros.sort()
print(numeros)
#invertir .reverse()
numeros = [5,3,7,8,2,1,4,6]
numeros.reverse()
print(numeros)
#index para saber la pocicion de una lista o cadena
numeros = [5,3,7,8,2,1,4,6]
print(numeros.index(7))
#.pop eliminar 
numeros = [5,3,7,8,2,1,4,6]
print(numeros.pop())
#pop eliminar un numero en concreto
numeros = [5,3,7,8,2,1,4,6]
eliminar = numeros.pop(3)
print(numeros)
print(eliminar)