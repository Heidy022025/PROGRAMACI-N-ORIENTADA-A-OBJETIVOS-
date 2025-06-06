# Clase base genérica
class Figura:
    def area(self):
        pass  # Se espera que las subclases implementen este método


# Clase Cuadrado que sobrescribe el método area()
class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


# Clase Circulo que también sobrescribe el método area()
class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.1416 * (self.radio ** 2)


# Prueba de polimorfismo: diferentes clases usan el mismo método de forma distinta
figuras = [Cuadrado(4), Circulo(3)]
for figura in figuras:
    print("Área:", figura.area())
