# EJERCICIO 3: Un hincha de fútbol desea conocer la cantidad de puntos que su
# equipo lleva acumulados en el campeonato, para ello recibe cada semana la
# información de la cantidad total de partidos, desde el inicio del campeonato, que
# el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
# recibe un punto, por cada partido ganado tres puntos y por los perdidos cero puntos.


win = int(input('Ingrese la cantidad de partidos GANADOS hasta ahora: '))
draw = int(input('Ingrese la cantidad de partidos EMPATADOS hasta ahora: '))
loss = int(input('Ingrese la cantidad de partidos PERDIDOS hasta ahora: '))
puntostotales = (win*3)+draw

print('Los puntos del equipo hasta ahora son: ', puntostotales, 'puntos.')