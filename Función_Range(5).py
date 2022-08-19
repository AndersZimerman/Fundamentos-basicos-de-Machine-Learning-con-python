#range(: : :)
print(list(range(2,7)))#Genera un rango de numeros especificados en el parametro
#Bucle for (en este caso se utiliza para que el resultado estese de manera vertical)
for i in range(2,7):
    print(i)
#De manera horizontal con end''
for i in range(2,7):
    print(i, end = ' - ')
#Range(, , , ) especificaar los saltos en el parametro del valor final
for i in range(1,10,2):
    print(f'El valor de i es:{i}')
#Otros ejemplos (invertir):
for i in reversed(range(0,10)):
    print(i)
#lista + range
lista = list(range(0,10))
print(f'Lista: {lista}')