#(Def definir una variable())
def función(nombre,edad):
    print(f'Hola, mi nombre es {nombre} con la edad de {edad} ')
función('Anders', 14)
#Suma
def Suma (num_1, num_2):
    respuesta = num_1 + num_2
    return respuesta #return Retorna el valor a la variable respuesta
print(Suma(5,4))
#Diferentes formas:
def Agregar ():
    respuesta = 50
    print(f'Numero {respuesta} ')
Agregar()
#Variable local y variable global
def función ():
    x = 50
    print('Variable local', x) #La variable local solo pertenece a la variable interna de la función, y solo se puede trabajar en la misma
x = 60
función()
print('Variable global', x) #Pertenece a la variable externa y se puede trabajar en la misma
