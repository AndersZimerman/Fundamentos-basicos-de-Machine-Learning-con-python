#diccionaria{'',''}
diccionario = {
    'nombre' : 'Anders',
    'edad' : 14
}
print(diccionario)
#Para llamar a un elmento(variable) en especifico alicamos [] y adentor el nombre de la variable
diccionario = {'nombre' : 'Anders','edad' : 14}
print(diccionario['nombre'])
print(diccionario['edad'])
#remplasar datos [especificamos el elemento y]con  = 'remplazamos' 
ciudad_remplazar = {'Asia':'Japón','Europa':'España'}
ciudad_remplazar['Asia'] = 'China'
print(ciudad_remplazar)
#Metodo update (actualiza nuestros datos cuando tengamos nuevos)
nombres_edades = {'Angel':15,'Carina':20,'Anders':14,'Tony':45}
nombres_edades.update({'José':20})#parametro ({})
print(nombres_edades)
#Metodo 'del' perimite eliminar un elemento en especifico 'elmento'
nombres_edades = {'Angel':15,'Carina':20,'Anders':14,'Tony':45}
del nombres_edades['Angel']#parametro []
print(nombres_edades)
#un Diccionario + una lista
nombres_edades = {'Angel':15,'Carina':20,'Anders':14,'Tony':45,'Maria': 47}
varones = {'Angel':15,'Anders':14,'Tony':45}
mujeres = {'Carina':20,'Maria': 47}
estudiantes = list(nombres_edades.keys())#pones como lista nombres_edades (antes era un diccionaria) con el parametro list()
                                         #keys() se utiliza para agregar un dato
estudiantes.sort()#sort()para ordenar
for e in estudiantes:#recorre el diccionario de estudiantes 'e' y crea una lista de 'estudiantes'
    print(" : ".join((e,str(nombres_edades[e]))))
    #joi() para combinar conjuntos de estudiantes, str([]) mostrara las posisiones dentro del dicionario
    #nombres_edades más el elemento que recorre cada una de las posiciones osea Estudiantes
