from abc import ABC, abstractmethod

# Clase abstracta que representa un vehículo genérico
class Vehiculo(ABC):
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    # Método abstracto: debe ser implementado por las subclases
    @abstractmethod
    def encender(self):
        pass

    # Otro método abstracto
    @abstractmethod
    def conducir(self):
        pass


# Clase Auto que hereda de Vehiculo e implementa sus métodos
class Auto(Vehiculo):
    def encender(self):
        print(f"{self.marca} {self.modelo} encendido con llave.")

    def conducir(self):
        print("El auto está en movimiento.")


# Clase Moto que también hereda de Vehiculo
class Moto(Vehiculo):
    def encender(self):
        print(f"{self.marca} {self.modelo} encendida con botón.")

    def conducir(self):
        print("La moto está en movimiento.")


# Prueba de abstracción
vehiculo1 = Auto("Toyota", "Corolla")
vehiculo1.encender()
vehiculo1.conducir()
