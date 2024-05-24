# En un nuevo diccionario llamado familia guardar 4 personas
# cada una de ellas con los mismos 5 datos
# (nombre, apellido, dni, email, fecha de nacimiento)

persona0 = {}
persona1 = {}
persona2 = {}
persona3 = {}

for i in range(4):
    if(i==0):
        print('A continuacion ingrese los datos de la PRIMERA PERSONA')
        persona0['nombre'] = input('Ingrese el nombre de la persona: ')
        persona0['apellido'] = input('Ingrese el apellido de la persona: ')
        persona0['DNI'] = input('Ingrese el DNI de la persona: ')
        persona0['email'] = input('Ingrese el email de la persona: ')
        persona0['fecha de nacimiento'] = str(input('Ingrese la fecha de nacimiento de la persona: '))
    elif(i==1):
        print('A continuacion ingrese los datos de la SEGUNDA PERSONA')
        persona1['nombre'] = input('Ingrese el nombre de la persona: ')
        persona1['apellido'] = input('Ingrese el apellido de la persona: ')
        persona1['DNI'] = input('Ingrese el DNI de la persona: ')
        persona1['email'] = input('Ingrese el email de la persona: ')
        persona1['fecha de nacimiento'] = str(input('Ingrese la fecha de nacimiento de la persona: '))
    elif(i==2):
        print('A continuacion ingrese los datos de la TERCERA PERSONA')
        persona2['nombre'] = input('Ingrese el nombre de la persona: ')
        persona2['apellido'] = input('Ingrese el apellido de la persona: ')
        persona2['DNI'] = input('Ingrese el DNI de la persona: ')
        persona2['email'] = input('Ingrese el email de la persona: ')
        persona2['fecha de nacimiento'] = str(input('Ingrese la fecha de nacimiento de la persona: '))
    elif(i==3):
        print('A continuacion ingrese los datos de la CUARTA PERSONA')
        persona3['nombre'] = input('Ingrese el nombre de la persona: ')
        persona3['apellido'] = input('Ingrese el apellido de la persona: ')
        persona3['DNI'] = input('Ingrese el DNI de la persona: ')
        persona3['email'] = input('Ingrese el email de la persona: ')
        persona3['fecha de nacimiento'] = str(input('Ingrese la fecha de nacimiento de la persona: '))


familia = {
    'persona1':persona0,
    'persona2':persona1,
    'persona3':persona2,
    'persona4':persona3
    }

print(familia)