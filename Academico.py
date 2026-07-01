alumno = ""
notas = []
opcion = 0


def registrar_alumno():
    nombre = input("Ingrese el nombre del alumno: ")
    return nombre


def registrar_notas():
    lista_notas = []

    for i in range(3):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1}: "))

                if nota >= 1.0 and nota <= 7.0:
                    lista_notas.append(nota)
                    break
                else:
                    print("La nota debe estar entre 1.0 y 7.0")

            except ValueError:
                print("Debe ingresar un numero valido")

    return lista_notas


def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    return promedio


def mostrar_estado(promedio):
    if promedio >= 4.0:
        print("Estado academico: Aprobado")
    else:
        print("Estado academico: Reprobado")


while opcion != 5:
    print("=== MINI ERP ACADEMICO ===")
    print("1. Registrar alumno")
    print("2. Registrar notas")
    print("3. Calcular promedio")
    print("4. Mostrar estado academico")
    print("5. Salir")

    try:
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            alumno = registrar_alumno()
            print("Alumno registrado correctamente")

        elif opcion == 2:
            if alumno != "":
                notas = registrar_notas()
                print("Notas registradas correctamente")
            else:
                print("Primero debe registrar un alumno")

        elif opcion == 3:
            if len(notas) > 0:
                promedio = calcular_promedio(notas)
                print("Alumno:", alumno)
                print("Promedio:", promedio)
            else:
                print("Primero debe registrar notas")

        elif opcion == 4:
            if len(notas) > 0:
                promedio = calcular_promedio(notas)
                print("Alumno:", alumno)
                mostrar_estado(promedio)
            else:
                print("Primero debe registrar notas")

        elif opcion == 5:
            print("Saliendo del sistema")

        else:
            print("Opcion no valida")

    except ValueError:
        print("Debe ingresar una opcion valida")


#ejercicio modificado
