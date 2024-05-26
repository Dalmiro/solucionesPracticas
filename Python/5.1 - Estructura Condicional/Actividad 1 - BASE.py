# Una despensa de barrio vende la leche de vaca entera de litro a 1000 pesos la unidad.
# Si el cliente compra más de 12  unidades (y hasta 24 unidades), el costo tiene un
# descuento del 10%. Si compra más de 24 unidades, el descuento es del 15%.
# Además posee la promoción a los jubilados. La promoción de jubilados es sumarle un
# 10% de descuento (si posee otros descuentos, se suma los descuentos).
# Desarrolle una solución algorítmica para saber cuento debe pagar el cliente.


precioporunidad = 1000
unidadescompradas = int(input('Ingrese cuantas unidades comprara: '))
jubilado = int(input('Por favor ingrese la opcion segun corresponda. \nOPCION 1: NO ES JUBILADO \nOPCION 2: ES JUBILADO \nSu opcion: '))
totalparcial = precioporunidad*unidadescompradas

if(jubilado==1):
    if(unidadescompradas < 12):
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalparcial, 'pesos,')
    elif(unidadescompradas>12 and unidadescompradas<24):
        totalconel10 = totalparcial*0.9
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalconel10, 'pesos,')
    elif(unidadescompradas>24):
        totalconel20 = totalparcial*0.8
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalconel20, 'pesos,')

if(jubilado==2):
    if(unidadescompradas < 12):
        totaljubilado = totalparcial*0.9
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubilado, 'pesos,')
    elif(unidadescompradas>12 and unidadescompradas<24):
        totaljubiladocon10 = totalparcial*0.8
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubiladocon10, 'pesos,')
    elif(unidadescompradas>24):
        totaljubiladocon20 = totalparcial*0.75
        print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubiladocon20, 'pesos,')