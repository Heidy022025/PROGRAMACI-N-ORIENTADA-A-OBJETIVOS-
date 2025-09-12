import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada.get()  # Obtiene el texto del campo
    if dato.strip() == "":  # Verifica que no esté vacío
        messagebox.showwarning("Advertencia", "Debe ingresar un dato válido.")
    else:
        lista_datos.insert(tk.END, dato)  # Agrega el dato al final de la lista
        entrada.delete(0, tk.END)  # Limpia el campo de texto

# Función para limpiar la selección o toda la lista
def limpiar_dato():
    seleccion = lista_datos.curselection()  # Verifica si hay un elemento seleccionado
    if seleccion:
        lista_datos.delete(seleccion)  # Elimina solo el seleccionado
    else:
        lista_datos.delete(0, tk.END)  # Si no hay selección, elimina todo

# Ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Datos - Aplicación GUI Básica")
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un dato:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Campo de texto
entrada = tk.Entry(ventana, width=30)
entrada.pack(pady=5)

# Botón Agregar
btn_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato, bg="lightgreen")
btn_agregar.pack(pady=5)

# Botón Limpiar
btn_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_dato, bg="lightcoral")
btn_limpiar.pack(pady=5)

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=40, height=10)
lista_datos.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()