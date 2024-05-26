precioporunidad = 1000
unidadescompradas = int(input('Ingrese cuantas unidades comprara: '))
jubilado = int(input('Por favor ingrese la opcion segun corresponda. \nOPCION 1: NO ES JUBILADO \nOPCION 2: ES JUBILADO \nSu opcion: '))
totalparcial = precioporunidad*unidadescompradas

#NO es jubilado
if(unidadescompradas < 12 and jubilado == 1):
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalparcial, 'pesos,')
elif(unidadescompradas>12 and unidadescompradas<24 and jubilado == 1):
    totalconel10 = totalparcial*0.9
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalconel10, 'pesos,')
elif(unidadescompradas>24 and jubilado == 1):
    totalconel20 = totalparcial*0.8
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totalconel20, 'pesos,')

#SI es jubilado
elif(unidadescompradas < 12 and not jubilado==1):
    totaljubilado = totalparcial*0.9
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubilado, 'pesos,')
elif(unidadescompradas>12 and unidadescompradas<24 and not jubilado==1):
    totaljubiladocon10 = totalparcial*0.8
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubiladocon10, 'pesos,')
elif(unidadescompradas>24 and not jubilado==1):
    totaljubiladocon20 = totalparcial*0.75
    print('El total a pagar por ', unidadescompradas, 'unidades es de ', totaljubiladocon20, 'pesos,')