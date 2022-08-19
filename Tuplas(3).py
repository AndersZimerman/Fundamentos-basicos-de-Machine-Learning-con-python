#Tupla()
tupla = (0,1,2,3,4)
print(tupla) 
#cocatenar (unir) tupla
tupla_a = (5,6,7,8,9)
tupla_b = ('uno','dos','tres')
print(tupla_a + tupla_b)
#replicar un dato
tupla_c = ('python ')*4
print(tupla_c)
#Metodo .count() sirve para ver cuantas veces se repite un elemento o dato
tupla = (1,4,3,3,6,7,2,4,5,5,5,5,7,6,5,3,5)
repetido = tupla.count(5)
print(repetido)
#Mentodo .index() sirve para allar la posision del primer elemento especificado en ()
tupla = (1,4,3,3,6,7,2,4,5,5,5,5,7,6,5,3,5)
Primero = tupla.index(5)
print(Primero)
#cambiar elemento en tupla o como modificar
#Antes
tupla_false = ('rojo','amarillo','verde')
tupla_false[1] = 'negro'
print(tupla_false)
#'tuple' object does not support item assignment
#(El objeto 'tuple' no admite la asignación de elementos)
#Despues
tupla = ('rojo','amarillo','verde')
lista = list(tupla)#transformamos la tupla en una lista con list
lista[1] = 'negro'#espcificamos la posiscion del dato a cambiar 
tupla = tuple(lista)# transformamos la lista a tupla con Tuple
print(tupla)
