# Programa: Calculador de áreas simples
# Función: permite al usuario calcular el area de un triángulo o de un rectángulo

def calcular_área_rectangulo(base:float, altura: float) -> float:
    """devuelve el área de un rectángulo: (base * altura)/ 2."""
    return (base * altura) / 2
def calcular_área_triangulo(base, altura):
    return (base * altura) / 2
# ----- Comienzo del programa -----
seguir: bool = True          # Booleano para controlar el bucle
while seguir:
    print("/nCalculador de áreas")
    print("1)rectángulo")
    print("2) triángulo")
    opcion: str = input("Elige una opción (1 ó 2):")

    if opcion =="1":
        # Pedimos datos al usuario
        base: float = float(input("Base (m): "))
        altura: float = float(input("Altura (m): "))
        area: float = calcular_área_rectangulo(base, altura)
        # Mostramos resultado
        print(f"Área del rectángulo: {area:.2f} m²")

    elif opcion == "2":
        base: float = float(input("Base (m): "))
        altura: float = float(input("Altura (m): "))
        area: float = calcular_área_triangulo(base, altura)
        print(f"Área del triángulo: {area:.2f} m²")
    else:
        print("Opción no válida.")
# Preguntamos si quiere otra operación
    respuesta: str = input("¿Calcular otra área? (s/n): ").lower()
    seguir = (respuesta == "si")  # Convierte la respuesta a booleano

print("¡Hasta luego!")