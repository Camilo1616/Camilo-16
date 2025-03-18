#listas 
estudiantes = []
cursos = ['java','python']
docentes = []
horarios = []   
# funcion para matricular un estudiante
def matricularEstudiante():
    nombre = input('Ingrese el nombre del estudiante: ')
    print ('Los cursos disponibles son: ')
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}') 
    
    cursoSeleccionado = int (input ('Seleccione el curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len (cursos):
        curso = cursos [cursoSeleccionado - 1]
        estudiante = {'nombre': nombre,'curso': curso}
        estudiantes.append (estudiante)
        print (f"estudiante {nombre} curso matriculado {curso}")
    else:
        print (f'Curso no disponible, recuerde que solo hay" {len (cursos)} cursos disponibles')
# funcion para asignar un docente
def asignarDocente():
    print ("seleccionar el curso para asignar un docente")
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}') 
    
    cursoSeleccionado = int (input ('Seleccione el curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len (cursos):
        curso = cursos [cursoSeleccionado - 1]
        nombreDocente = input ('Ingrese el nombre del docente: ')
        docente = {'nombre': nombreDocente,'curso': curso}
        docentes.append (docente)
        print (f"docente {nombreDocente} asignado al curso {curso}")
    else:
        print (f'Curso no disponible, recuerde que solo hay" {len (cursos)} cursos disponibles')

# funcion para asignar horario a un curso 
def asignarHorario():
    print ("seleccionar el curso para asignar un horario")
    for i, curso in enumerate(cursos):
        print(f'{i+1}: {curso}') 
    
    cursoSeleccionado = int (input ('Seleccione el curso: '))
    if cursoSeleccionado > 0 and cursoSeleccionado <= len (cursos):
        curso = cursos [cursoSeleccionado - 1] 
        dias = input ('Ingrese los dias de clase (ej: martes y jueves): ')
        hora = input ('Ingrese la hora de inicio (ej: 18:00): ')
        horarioClase = {'dias': dias,'hora': hora,'curso': curso}
        horarios.append (horarioClase)
        print (f'horario asignado al curso {curso}, dias de clase {dias} y hora de inicio {hora}')
    else:
        print (f'Curso no disponible, recuerde que solo hay" {len (cursos)} cursos disponibles')

def mostrarEstudiantes():
    if estudiantes:
        print ('Listado de estudiantes matriculados')
        for estudiante in estudiantes:
            print (f"nombre: {estudiante['nombre']}, curso: {estudiante['curso']}")
    else:
        ("No hay estudiantes matriculados")
        
def MostrarDocentes():
    if docentes:
        print ('Listado de docentes matriculados')
        for docente in docentes:
            print (f"nombre: {docente['nombre']}, curso: {docente['curso']}")
    else: 
        ("No hay docentes asignados")

def mostrarHorarios():
    if horarios:
        print ('\nHorarios de los cursos')
        for horario in horarios:
            print (f"curso {horario['curso']}, dias: {horario['dias']}, hora: {horario['hora']} ")
    else: 
        ("No hay docentes asignados")

# menu 
while True:
    print ('\n sistema de matricula de Dev senior')
    print ('1. Matricular estudiante')
    print ('2. Asignar docente a un curso')
    print ('3. Asignar horario a un curso ')
    print ('4. Mostrar la lista de estudiantes matriculados')
    print ('5. Mostrar lista de docentes asignados')
    print ('6. Mostrar horarios de los cursos')
    print ('7. Salir')
    
    opcion = int(input('Seleccione una opcion: '))

    if opcion == 1:
        matricularEstudiante()
    elif opcion == 2:
        asignarDocente()
    elif opcion == 3:
        asignarHorario()
    elif opcion == 4:
        mostrarEstudiantes()
    elif opcion == 5:
        MostrarDocentes()
    elif opcion == 6:
        mostrarHorarios()
    elif opcion == 7:
        print ('Gracias por usar el sistema')
        break
    else:
        print ('opcion no valida')
