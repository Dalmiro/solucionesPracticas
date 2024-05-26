Algoritmo calcular_costo_leche
    Definir precioporunidad, unidadescompradas, jubilado, totalparcial, totalconel10, totalconel20, totaljubilado, totaljubiladocon10, totaljubiladocon20 Como Entero
	
    Escribir "Ingrese cuántas unidades comprará: "
    Leer unidadescompradas
    Escribir "Por favor, ingrese la opción según corresponda:"
    Escribir "OPCION 1: NO ES JUBILADO"
    Escribir "OPCION 2: ES JUBILADO"
    Escribir "Su opción: "
    Leer jubilado
	
    totalparcial = precioporunidad * unidadescompradas
	
    Si unidadescompradas < 12 y jubilado = 1 Entonces
        Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalparcial, " pesos."
    Sino Si unidadescompradas > 12 y unidadescompradas < 24 y jubilado = 1 Entonces
			totalconel10 = totalparcial * 0.9
			Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalconel10, " pesos."
		Sino Si unidadescompradas > 24 y jubilado = 1 Entonces
				totalconel20 = totalparcial * 0.8
				Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalconel20, " pesos."
			Sino Si unidadescompradas < 12 y jubilado = 2 Entonces
					totaljubilado = totalparcial * 0.9
					Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubilado, " pesos."
				Sino Si unidadescompradas > 12 y unidadescompradas < 24 y jubilado = 2 Entonces
						totaljubiladocon10 = totalparcial * 0.8
						Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubiladocon10, " pesos."
					Sino Si unidadescompradas > 24 y jubilado = 2 Entonces
							totaljubiladocon20 = totalparcial * 0.75
							Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubiladocon20, " pesos."
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
FinAlgoritmo