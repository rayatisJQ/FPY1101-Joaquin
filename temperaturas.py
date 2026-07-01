temperaturas = []
suma = 0



for i in range(5):
    temperaturas.append = int(input(f"Ingrese la temperatura numero {i+1}: "))

    if temperaturas > -20 and temperaturas < 20:
        print("Temperatura registrada correctamente")
    else:
        print("Temperatura no valida dentro del rango")
    
for temperatura in temperaturas:
    suma += temperatura

promedio = suma / len(temperaturas)

print(promedio)
# Version mejorada del ejercicio 1
