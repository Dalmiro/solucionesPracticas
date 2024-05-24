# EJERCICIO 2: Un pintor de casas debe hacer un presupuesto para un cliente. Lo
# que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
# cliente le indica que necesita conocer el costo de mano de obra para pintar una
# pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
# cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
# pintar la pared.


precioporm2 = int(input('ingrese cuantos se cobrara POR CADA metro cuadrado a pintar: '))
totalapintar = int(input('ingrese cuantos metros cuadrados TOTALES se deben pintar: '))
presupuesto = precioporm2*totalapintar

print('El presupuesto para la cantidad de metros cuadrados ingresada es de: ', presupuesto, ' pesos.')
