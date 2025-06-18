# Esta clase representa un producto que se puede vender
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre  # Nombre del producto
        self.precio = precio  # Precio del producto
        self.stock = stock    # Cantidad en inventario

    # Mostrar los datos del producto
    def mostrar(self):
        print("Producto:", self.nombre)
        print("Precio: $", self.precio)
        print("Stock:", self.stock)


# Esta clase representa un cliente que compra cosas
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []  # Aquí se guardan los productos que compra

    # Agregar un producto al carrito si hay suficiente stock
    def agregar_producto(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.stock -= cantidad  # Se descuenta del stock
            print(f"{cantidad} x {producto.nombre} agregado al carrito.")
        else:
            print("No hay suficiente stock de", producto.nombre)

    # Ver lo que tiene en el carrito
    def ver_carrito(self):
        print("Carrito de", self.nombre)
        total = 0
        for producto, cantidad in self.carrito:
            print(producto.nombre, "x", cantidad, " = $", producto.precio * cantidad)
            total += producto.precio * cantidad
        print("Total a pagar: $", total)


# Esta clase representa la tienda donde se venden los productos
class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista de productos disponibles

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Bienvenido a", self.nombre)
        print("Productos disponibles:")
        for p in self.productos:
            p.mostrar()


# Ahora empezamos a usar las clases

# Crear productos
prod1 = Producto("Cuaderno", 2.5, 10)
prod2 = Producto("Lápiz", 0.5, 20)
prod3 = Producto("Mochila", 15.0, 5)

# Crear tienda y agregar los productos
mi_tienda = Tienda("Librería Escolar")
mi_tienda.agregar_producto(prod1)
mi_tienda.agregar_producto(prod2)
mi_tienda.agregar_producto(prod3)

# Mostrar los productos de la tienda
mi_tienda.mostrar_productos()

# Crear un cliente y hacer una compra
cliente1 = Cliente("Pedro")
cliente1.agregar_producto(prod1, 10)
cliente1.agregar_producto(prod3, 1)

# Ver el carrito final
cliente1.ver_carrito()
