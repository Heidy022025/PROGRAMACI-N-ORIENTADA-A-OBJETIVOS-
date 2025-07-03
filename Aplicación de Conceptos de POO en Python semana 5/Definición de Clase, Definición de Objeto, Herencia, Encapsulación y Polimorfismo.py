from math import pi

# Clase base que representa una figura geométrica
class Figura:
    def __init__(self, color: str = "sin color") -> None:
        self.color = color  # Atributo público

    def area(self) -> float:
        # Método que será sobrescrito por las clases hijas (polimorfismo)
        raise NotImplementedError("Este método debe ser implementado en la subclase")


# Clase derivada que representa un rectángulo (hereda de Figura)
class Rectangulo(Figura):
    def __init__(self, base: float, altura: float, color: str = "sin color") -> None:
        super().__init__(color)  # Llama al constructor de la clase base
        self.__base = base     # Atributo privado (encapsulado)
        self.__altura = altura # Atributo privado (encapsulado)

    # Getter para base
    @property
    def base(self) -> float:
        return self.__base

    # Setter para base con validación
    @base.setter
    def base(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("La base debe ser mayor que cero")
        self.__base = valor

    # Getter para altura
    @property
    def altura(self) -> float:
        return self.__altura

    # Setter para altura con validación
    @altura.setter
    def altura(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("La altura debe ser mayor que cero")
        self.__altura = valor

    # Método sobrescrito que calcula el área del rectángulo (polimorfismo)
    def area(self) -> float:
        return self.__base * self.__altura


# Clase derivada que representa un círculo (hereda de Figura)
class Circulo(Figura):
    def __init__(self, radio: float, color: str = "sin color") -> None:
        super().__init__(color)
        self.__radio = radio  # Atributo privado (encapsulado)

    @property
    def radio(self) -> float:
        return self.__radio

    @radio.setter
    def radio(self, valor: float) -> None:
        if valor <= 0:
            raise ValueError("El radio debe ser mayor que cero")
        self.__radio = valor

    # Método sobrescrito que calcula el área del círculo (polimorfismo)
    def area(self) -> float:
        return pi * (self.__radio ** 2)


# Bloque principal: se ejecuta solo si el archivo se ejecuta directamente
if __name__ == "__main__":
    # Crear objetos de las clases derivadas (herencia)
    rect = Rectangulo(base=8, altura=5, color="rojo")
    circ = Circulo(radio=4, color="azul")

    # Lista de figuras para mostrar polimorfismo
    figuras = [rect, circ]

    # Mostrar resultados
    for figura in figuras:
        print(f"{figura.__class__.__name__} de color {figura.color} tiene un área de {figura.area():.2f}")
