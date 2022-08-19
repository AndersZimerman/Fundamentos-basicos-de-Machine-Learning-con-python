# 
#Ejemplo basico
#dividir la palabra 'Python' por letras y ponerlo en una lista
lista = []
for letras in 'Python':
    lista.append(letras)
print(lista)
#ejemplo 'comprimido'
lista = [letras for letras in 'Python']
print(lista)
#Rellenar una lista a otra
lista_a = [1,2,3,4,5,6,7]
lista_b = []
for lis in lista_a:
    para_lista_b = lis
    lista_b.append(para_lista_b)
print(lista_b)
#ejemplo 'comprimido'
lista_a = [1,2,3,4,5,6,7]
lista_b = [lis for lis in lista_a]
print(lista_b)