# Un profesor de matemática necesita generar la tabla de multiplicar de un número entero
# comprendido entre 1 y 10.

numerotabla = int(input('Ingrese el numero: '))

for i in range(11):
    multiplicacion = numerotabla*i
    print(numerotabla,'x',i,'=',multiplicacion)