# definimos una clase
class Libro:
    def __init__(self,titulo,autor,categoria,isbn):
        self.datos_principales = (titulo,autor)
        self.categoria = categoria
        self.isbn = isbn

    def mostrar_info(self):
        titulo, autor = self.datos_principales
        return f"Título: {titulo}, Autor: {autor}, Categoría: {self.categoria}, ISBN: {self.isbn}"
#definimos la clase usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, isbn):
        for libro in self.libros_prestados:
            if libro.isbn == isbn:
                self.libros_prestados.remove(libro)
                return libro
        return None

    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return f"{self.nombre} no tiene libros prestados."
        return "\n".join([libro.mostrar_info() for libro in self.libros_prestados])
#definimos la clase biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario ISBN -> Libro
        self.usuarios = {}  # Diccionario ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # Dentro de la clase Biblioteca
    def prestar_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible.")
            return
        libro = self.libros.pop(isbn)  # quitar de libros disponibles
        self.usuarios[id_usuario].prestar_libro(libro)
        print(f"Libro '{libro.datos_principales[0]}' prestado a {self.usuarios[id_usuario].nombre}.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario not in self.usuarios:
            print("Usuario no registrado.")
            return
        libro = self.usuarios[id_usuario].devolver_libro(isbn)
        if libro:
            self.libros[isbn] = libro  # vuelve a estar disponible
            print(f"Libro '{libro.datos_principales[0]}' devuelto a la biblioteca.")
        else:
            print("El usuario no tenía prestado ese libro.")

    # funcion para añadir libros
    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.datos_principales[0]}' añadido a la biblioteca.")
        else:
            print("Este libro ya existe en la biblioteca.")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            eliminado = self.libros.pop(isbn)
            print(f"Libro '{eliminado.datos_principales[0]}' eliminado de la biblioteca.")
        else:
            print("No se encontró un libro con ese ISBN.")
    # gestionamos el usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario '{usuario.nombre}' registrado correctamente.")
        else:
            print("Ya existe un usuario con ese ID.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            eliminado = self.usuarios.pop(id_usuario)
            self.ids_usuarios.remove(id_usuario)
            print(f"Usuario '{eliminado.nombre}' dado de baja.")
        else:
            print("No se encontró un usuario con ese ID.")
    # funcion para poder buscar el libro
    def buscar_libros(self, clave):
        resultados = []
        for libro in self.libros.values():
            titulo, autor = libro.datos_principales
            if (clave.lower() in titulo.lower() or
                    clave.lower() in autor.lower() or
                    clave.lower() in libro.categoria.lower()):
                resultados.append(libro.mostrar_info())

        if resultados:
            return "\n".join(resultados)
        else:
            return "No se encontraron libros con esa búsqueda."
# probamos el sitema
if __name__ == "__main__":
    # Crear biblioteca
    biblio = Biblioteca()

    # Añadir libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "Novela", "12345")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Fábula", "67890")
    biblio.añadir_libro(libro1)
    biblio.añadir_libro(libro2)

    # Registrar usuarios
    usuario1 = Usuario("Heidy", 1)
    usuario2 = Usuario("Carlos", 2)
    biblio.registrar_usuario(usuario1)
    biblio.registrar_usuario(usuario2)

    # Prestar libro
    biblio.prestar_libro(1, "12345")

    # Listar libros prestados por un usuario
    print("\nLibros prestados por Heidy:")
    print(usuario1.listar_libros_prestados())

    # Devolver libro
    biblio.devolver_libro(1, "12345")

    # Buscar libros
    print("\nBúsqueda por 'Fábula':")
    print(biblio.buscar_libros("Fábula"))