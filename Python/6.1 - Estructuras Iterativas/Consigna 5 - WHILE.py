# Un profesor de matemática necesita generar la tabla de multiplicar de un número entero
# comprendido entre 1 y 10.

numerotabla = int(input('Ingrese el numero: '))
cont = 0

while(numerotabla<=10):
    multiplicacion = numerotabla*cont
    cont = cont+1
    print(numerotabla,'x',cont,'=',multiplicacion)
    if(cont==10):
        break
