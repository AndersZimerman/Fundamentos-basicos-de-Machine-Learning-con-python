from multiprocessing.reduction import duplicate


def multiplicar_por (n):
  return lambda x: x * n
 
duplicar = multiplicar_por(2)
triplicar = multiplicar_por(3)
diez_veces = multiplicar_por(10)
a = 4
lambda x : a
print()