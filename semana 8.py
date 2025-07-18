import os
import subprocess


# ======== Funciones auxiliares =========

def mostrar_codigo(ruta_script):
    """Muestra el contenido completo del archivo Python."""
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def mostrar_descripcion_script(ruta_script):
    """Muestra el docstring del script como descripción si está disponible."""
    try:
        with open(ruta_script, 'r') as archivo:
            primera_linea = archivo.readline()
            if primera_linea.strip().startswith('"""'):
                descripcion = primera_linea.strip('"""\n ')
                print(f"📘 Descripción: {descripcion}")
            else:
                print("Este script no contiene una descripción (docstring).")
    except Exception as e:
        print(f"Ocurrió un error al leer la descripción: {e}")


def ejecutar_codigo(ruta_script):
    """Ejecuta un script Python en consola."""
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux/macOS
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


# ========= Menú principal ============

def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2',
        '3': 'Unidad 3'
    }

    while True:
        print("\n===== 📂 MENÚ PRINCIPAL - DASHBOARD POO =====")
        for key, value in unidades.items():
            print(f"{key} - {value}")
        print("0 - ❌ Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            ruta_unidad = os.path.join(ruta_base, unidades[eleccion_unidad])
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print("⚠️ La carpeta de la unidad no existe.")
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")


# ========= Submenús por unidad ==========

def mostrar_sub_menu(ruta_unidad):
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print(f"\n📁 SUBMENÚ - {os.path.basename(ruta_unidad)}")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - 🔙 Volver al menú principal")

        eleccion = input("Selecciona una subcarpeta o '0' para regresar: ")
        if eleccion == '0':
            break
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[indice]))
            else:
                print("⚠️ Opción inválida.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")


# ========= Mostrar scripts disponibles ==========

def mostrar_scripts(ruta_sub_carpeta):
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    while True:
        print(f"\n📜 SCRIPTS EN: {os.path.basename(ruta_sub_carpeta)}")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - 🔙 Volver al submenú anterior")
        print("9 - 🏠 Volver al menú principal")

        eleccion = input("Elige un script, '0' o '9': ")
        if eleccion == '0':
            break
        elif eleccion == '9':
            return
        try:
            indice = int(eleccion) - 1
            if 0 <= indice < len(scripts):
                ruta_script = os.path.join(ruta_sub_carpeta, scripts[indice])
                mostrar_descripcion_script(ruta_script)
                codigo = mostrar_codigo(ruta_script)

                if codigo:
                    ejecutar = input("¿Deseas ejecutar este script? (1 = Sí / 0 = No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)
                    elif ejecutar == '0':
                        print("No se ejecutó el script.")
                input("\nPresiona Enter para volver.")
            else:
                print("⚠️ Opción inválida.")
        except ValueError:
            print("⚠️ Ingresa un número válido.")


# ========== Inicio del programa ==========

if __name__ == "__main__":
    mostrar_menu()
