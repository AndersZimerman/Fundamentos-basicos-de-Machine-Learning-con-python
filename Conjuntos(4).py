#Conjuntos (set{}) 
conjunto = {0,1,2,3,4}
print(conjunto)
#podemos mesclar diferentes tipos de datos dentro de un conjunto
set = {0,1,2,3,4,'python',('w','A')}
print(set)
#añadir un dato .add()
set = {0,1,2,3,4}
set.add(5)
print(set)
#Eliminar (limpiar) todos los datos de un conjunto .clear()
set = {0,1,2,3,4}
set.clear()
print(set)
#Descartar un dato en especifico .discard()
set = {0,1,2,3,4}
set.discard(4)#valor, no posiscion
print(set)
#Eliminar un dato en especifico .remove()
set = {0,1,2,3,4}
set.remove(4)#valor, no posiscion
print(set)
# Diferencia ente .discard() descarta el dato no lo elimina y .remove() elimina el dato
# al momento de bucar el dato saldra error pero en .discar() no 
#Union, unir dos conjuntos 
set_a = {0,1,2,3,4,5,}
set_b = {4,5,6,7,8,9}
print(set_a | set_b)
# no se repite (4,5)
# Interseccion solo toma en cuenta los datos repetido o compartidos como 4,5
set_a = {0,1,2,3,4,5,}
set_b = {4,5,6,7,8,9}
print(set_a & set_b)
# Sin datos repetidos:
set_a = {0,1,2,3,4,5,}
set_b = {6,7,8,9}
print(set_a & set_b)
#solo aparece el set() vacio
# Ver solo el set_a (con datos repetidos)
set_a = {0,1,2,3,4,5,}
set_b = {4,5,6,7,8,9}
print(set_a - set_b)
# Diferencia simetrica (con datos repetidos)
set_a = {0,1,2,3,4,5,}
set_b = {4,5,6,7,8,9}
print(set_a ^ set_b)#no se imprime los datos repetidos