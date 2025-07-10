# Clase que simula una impresora virtual que se activa y desactiva
class ImpresoraVirtual:
    def __init__(self, modelo):
        """
        Constructor: se ejecuta cuando se crea el objeto.
        Simula encender la impresora virtual.
        """
        self.modelo = modelo
        self.activa = True
        print(f"Impresora '{self.modelo}' encendida y lista para imprimir.")

    def imprimir_documento(self, documento):
        """
        Método que simula la impresión de un documento.
        """
        if self.activa:
            print(f"Imprimiendo documento: '{documento}' en la impresora '{self.modelo}'...")
        else:
            print("Error: La impresora está apagada.")

    def __del__(self):
        """
        Destructor: se ejecuta cuando el objeto se destruye.
        Simula apagar la impresora virtual.
        """
        if self.activa:
            print(f"Impresora '{self.modelo}' apagada automáticamente.")
        else:
            print(f"Objeto de la impresora '{self.modelo}' eliminado.")


# ---------- Uso de la clase ImpresoraVirtual ----------

# Crear una impresora virtual
mi_impresora = ImpresoraVirtual("Canon-Virtual-3000")

# Imprimir un documento
mi_impresora.imprimir_documento("Tarea_Matematicas.pdf")

# Eliminar el objeto para activar el destructor
del mi_impresora
