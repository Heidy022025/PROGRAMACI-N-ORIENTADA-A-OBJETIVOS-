# Clase base
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido.")


# Clase hija que hereda de Animal
class Perro(Animal):
    def hablar(self):
        # Sobrescribe el método hablar
        print(f"{self.nombre} dice: Guau!")


# Otra clase hija que hereda de Animal
class Gato(Animal):
    def hablar(self):
        print(f"{self.nombre} dice: Miau!")


# Prueba de herencia
p = Perro("Firulais")
g = Gato("Michi")
p.hablar()
g.hablar()
