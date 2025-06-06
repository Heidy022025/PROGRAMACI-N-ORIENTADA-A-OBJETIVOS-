class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.__salario = salario  # atributo privado (encapsulado)

    def mostrar_info(self):
        # Método para mostrar el salario (acceso controlado)
        print(f"Empleado: {self.nombre}, Salario: {self.__salario}")

    def aumentar_salario(self, porcentaje):
        # Método para modificar el salario con lógica segura
        if porcentaje > 0:
            self.__salario += self.__salario * (porcentaje / 100)


# Prueba de encapsulación
emp = Empleado("Lucía", 1000)
emp.mostrar_info()
emp.aumentar_salario(10)
emp.mostrar_info()
