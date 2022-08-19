#Map devuelve un objeto de asignación (un iterador) que podemos usar en otras partes de nuestro programa
def mult(n):
    return n * 5
lista = [0,1,2,3,4,5,6,7]
lista_map = list(map(mult,lista)) #Map aplicara lo puesto en el primer parametro al segundo y luego almacenara el resultado en la variable lista_map
print(lista_map)
#Tupla
def nombres(n):
    return n.upper()
tupla = ('José','Ana','Luis','Tony')
tupla_nombres = tuple(map(nombres,tupla)) #Funciones, elementos iterables
print(tupla_nombres)
#Filter 'filtra los elementos de los parametros filter( , )'
#Ejemplo:
def impares(i):
    if(i % 2 == 1 ):
        return i
numeros = [0,1,2,3,4,5,6,7]
numero_impares = list(filter(impares,numeros))
print(numero_impares)
