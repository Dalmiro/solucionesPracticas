# Mostrar sólo los números pares desde 0 hasta el número ingresado (input).

numerosolicitado = int(input('Ingrese un numero mayor a 0: '))

for i in range (numerosolicitado):
    i = (i+1)
    if(i%2==0):
        print(i)