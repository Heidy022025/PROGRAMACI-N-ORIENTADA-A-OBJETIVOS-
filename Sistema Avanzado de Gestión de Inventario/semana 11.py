# ========================================
# Clase Producto (POO)
# ========================================
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


# ========================================
# Clase Inventario con persistencia
# ========================================
import json

class Inventario:
    def __init__(self):
        self.productos = {}  # clave: id_producto, valor: objeto producto

    # Añadir producto
    def anadir_producto(self, producto):
        if producto.id_producto in self.productos:
            print("❌ Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("✅ Producto eliminado.")
        else:
            print("❌ No existe ese ID en el inventario.")

    # Actualizar cantidad
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
            self.productos[id_producto].cantidad = nueva_cantidad
            print("✅ Cantidad actualizada.")
        else:
            print("❌ No existe ese ID.")

    # Actualizar precio
    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].precio = nuevo_precio
            print("✅ Precio actualizado.")
        else:
            print("❌ No existe ese ID.")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return resultados

    # Guardar en archivo JSON
    def guardar_json(self, archivo):
        with open(archivo, "w") as f:
            data = {pid: vars(p) for pid, p in self.productos.items()}
            json.dump(data, f, indent=2)

    # Cargar desde archivo JSON
    def cargar_json(self, archivo):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)
                for pid, atributos in data.items():
                    self.anadir_producto(Producto(**atributos))
        except FileNotFoundError:
            pass


# ========================================
# Menú de consola
# ========================================
def menu():
    inventario = Inventario()
    inventario.cargar_json("inventario.json")

    while True:
        print("\n==== MENÚ INVENTARIO ====")
        print("1. Añadir producto")
        print("2. Mostrar todos los productos")
        print("3. Eliminar producto")
        print("4. Actualizar cantidad")
        print("5. Actualizar precio")
        print("6. Buscar producto por nombre")
        print("0. Salir")
        opcion = input("Opción: ")

        if opcion == "1":
            idp = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.anadir_producto(Producto(idp, nombre, cantidad, precio))
            inventario.guardar_json("inventario.json")

        elif opcion == "2":
            if inventario.productos:
                for p in inventario.productos.values():
                    print(p.__dict__)
            else:
                print("Inventario vacío.")

        elif opcion == "3":
            idp = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(idp)
            inventario.guardar_json("inventario.json")

        elif opcion == "4":
            idp = input("ID del producto: ")
            nueva_cantidad = int(input("Nueva cantidad: "))
            inventario.actualizar_cantidad(idp, nueva_cantidad)
            inventario.guardar_json("inventario.json")

        elif opcion == "5":
            idp = input("ID del producto: ")
            nuevo_precio = float(input("Nuevo precio: "))
            inventario.actualizar_precio(idp, nuevo_precio)
            inventario.guardar_json("inventario.json")

        elif opcion == "6":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(nombre)
            if resultados:
                for p in resultados:
                    print(p.__dict__)
            else:
                print("No se encontraron productos con ese nombre.")

        elif opcion == "0":
            print("Guardando y saliendo...")
            inventario.guardar_json("inventario.json")
            break

        else:
            print("❌ Opción no válida.")


if __name__ == "__main__":
    menu()