def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    carrera = input("Ingrese su carrera: ")

    return nombre, carrera


def registrar_libro():
    libro = input("Ingrese el nombre del libro: ")

    while True:
        try:
            dias = int(input("Ingrese los dias de prestamo: "))

            if dias > 0:
                return libro, dias
            else:
                print("Los dias deben ser mayor a 0")

        except ValueError:
            print("Debe ingresar un numero valido")


def generar_resumen(nombre, carrera, libro, dias):
    print("=== RESUMEN DE RESERVA ===")
    print("Nombre:", nombre)
    print("Carrera:", carrera)
    print("Libro:", libro)
    print("Dias de prestamo:", dias)

    if dias > 14:
        print("Advertencia: supera los 14 dias de prestamo")
    else:
        print("Prestamo dentro del plazo permitido")


print("=== SISTEMA DE RESERVAS DE BIBLIOTECA ===")

nombre, carrera = registrar_usuario()
libro, dias = registrar_libro()
generar_resumen(nombre, carrera, libro, dias)
#ejercicio modificado
