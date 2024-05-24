cantestudiantes = int(input('Ingrese la cantidad de estudiantes que tomaron el examen: '))
notas = []
sumatoriadenotas = 0

for i in range(cantestudiantes):
    notaindividual = input('Ingrese la nota del estudiante: ')
    notas.append(notaindividual)

for i in range(len(notas)):
    sumatoriadenotas += int(notas[i])
    promedionotas = sumatoriadenotas/cantestudiantes

if(promedionotas > 8):
    print('El promedio general de los alumnos en el exmaen es de', promedionotas, '. Es ELEVADO')
elif(promedionotas >= 6 and promedionotas <= 8):
    print('El promedio general de los alumnos en el exmaen es de: ', promedionotas, '. Es ACEPTABLE')
elif(promedionotas <6):
    print('El promedio general de los alumnos en el exmaen es de: ', promedionotas, '. Es BAJO')