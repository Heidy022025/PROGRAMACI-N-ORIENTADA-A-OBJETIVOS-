# Programación Orientada a Objetos (POO)
# Ejemplo: Registro y promedio de temperaturas semanales
# Clase base que representa el registro de temperaturas durante una semana
class RegistroTemperaturas:
    def __init__(self):
        # Encapsulamiento: usamos una lista protegida para almacenar las temperaturas
        self._temperaturas = []

    # Método para registrar 7 temperaturas ingresadas por el usuario
    def registrar(self):
        for i in range(7):  # 7 días de la semana
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
                    self._temperaturas.append(temp)
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número.")

    # Método para calcular el promedio de las temperaturas registradas
    def calcular_promedio(self):
        return sum(self._temperaturas) / len(self._temperaturas)

    # Método para mostrar los resultados: lista de temperaturas y su promedio
    def mostrar_resultado(self):
        print("\n--- Resultados del Registro de Temperaturas ---")
        print("Temperaturas registradas:", self._temperaturas)
        print("Promedio semanal:", round(self.calcular_promedio(), 2))


# Clase derivada (subclase) que extiende la funcionalidad de RegistroTemperaturas
class RegistroExtendido(RegistroTemperaturas):
    def __init__(self):
        # Llamamos al constructor de la clase base
        super().__init__()

    # Polimorfismo: redefinimos el método mostrar_resultado
    def mostrar_resultado(self):
        # Llamamos al método original de la clase base para no repetir código
        super().mostrar_resultado()


# --- Programa principal ---

# Creamos una instancia de la clase hija (RegistroExtendido)
# Aquí se aplica HERENCIA y POLIMORFISMO
registro = RegistroExtendido()

# Llamamos al método para ingresar temperaturas
registro.registrar()

# Llamamos al método para mostrar todos los resultados
registro.mostrar_resultado()