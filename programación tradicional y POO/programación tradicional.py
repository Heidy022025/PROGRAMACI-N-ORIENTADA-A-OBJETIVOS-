# Programación Tradicional
# Ejemplo: Registro y promedio de temperaturas semanales

# Definición de variables globales
temperaturas = []
dias_semana = 7

# Función para registrar temperaturas
def registrar_temperaturas():
    global temperaturas
    for i in range(dias_semana):
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")

# Función para calcular el promedio
def calcular_promedio():
    global temperaturas
    return sum(temperaturas) / len(temperaturas)

# Uso de las funciones en la programación tradicional
registrar_temperaturas()
promedio = calcular_promedio()

# Imprimir resultado final
print("Temperaturas (Tradicional):", temperaturas)
print("Promedio semanal (Tradicional):", round(promedio, 2))