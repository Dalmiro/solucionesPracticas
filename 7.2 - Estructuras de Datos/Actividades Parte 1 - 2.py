# Eliminar la tercer y la última persona de la lista del ejercicio 1
# luego ordenar la lista y mostrarlo

nombres = []

for i in range(10):
    nombres.append(input('Ingrese un nombre: '))

print(nombres)

nombres.pop(2)
nombres.pop()
print(nombres)

nombres.sort()
print(nombres)