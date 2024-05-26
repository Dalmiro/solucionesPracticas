Algoritmo calcular_costo_leche
    Definir precioporunidad, unidadescompradas, jubilado, totalparcial Como Entero
    
    Escribir "Ingrese cuántas unidades comprará: "
    Leer unidadescompradas
    Escribir "Por favor, ingrese la opción según corresponda:"
    Escribir "OPCION 1: NO ES JUBILADO"
    Escribir "OPCION 2: ES JUBILADO"
    Escribir "Su opción: "
    Leer jubilado
    
    totalparcial = precioporunidad * unidadescompradas

    Si jubilado = 1 Entonces
		Si unidadescompradas < 12 Entonces
            Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalparcial, " pesos."
        Sino Si unidadescompradas > 12 Y unidadescompradas < 24 Entonces
				totalconel10 = totalparcial * 0.9
				Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalconel10, " pesos."
			Sino Si unidadescompradas > 24 Entonces
					totalconel20 = totalparcial * 0.85
					Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totalconel20, " pesos."
				FinSi
			FinSi
		FinSi
	FinSi
				Si jubilado = 2 Entonces
					Si unidadescompradas < 12 Entonces
						totaljubilado = totalparcial * 0.9
						Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubilado, " pesos."
					Sino Si unidadescompradas > 12 Y unidadescompradas < 24 Entonces
							totaljubiladocon10 = totalparcial * 0.8
							Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubiladocon10, " pesos."
						Sino Si unidadescompradas > 24 Entonces
								totaljubiladocon20 = totalparcial * 0.75
								Escribir "El total a pagar por ", unidadescompradas, " unidades es de ", totaljubiladocon20, " pesos."
							FinSi
						FinSi
					FinSi
				FinSi
FinAlgoritmo

