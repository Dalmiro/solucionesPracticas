Algoritmo generar_tabla_multiplicar
    Definir numerotabla, cont, multiplicacion Como Entero
    
    Escribir "Ingrese el número para generar la tabla de multiplicar: "
    Leer numerotabla
    
    cont = 0
    
    Mientras numerotabla <= 10 y cont <= 10 Hacer
        multiplicacion = numerotabla * cont
        cont = cont + 1
        Escribir numerotabla, " x ", cont, " = ", multiplicacion
    FinMientras
FinAlgoritmo