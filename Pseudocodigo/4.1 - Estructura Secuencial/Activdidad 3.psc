Algoritmo calcular_puntos_equipo
    Definir win, draw, loss, puntostotales Como Entero
    
    Escribir "Ingrese la cantidad de partidos GANADOS hasta ahora: "
    Leer win
    Escribir "Ingrese la cantidad de partidos EMPATADOS hasta ahora: "
    Leer draw
    Escribir "Ingrese la cantidad de partidos PERDIDOS hasta ahora: "
    Leer loss
    
    puntostotales = (win * 3) + draw
    
    Escribir "Los puntos del equipo hasta ahora son: ", puntostotales, " puntos."
FinAlgoritmo