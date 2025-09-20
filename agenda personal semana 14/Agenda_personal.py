import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesita instalación: pip install tkcalendar

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Agenda Personal")
ventana.geometry("650x400")

# Dividir la interfaz en 3 secciones con Frames
frame_lista = ttk.Frame(ventana, padding=10)
frame_entradas = ttk.Frame(ventana, padding=10)
frame_botones = ttk.Frame(ventana, padding=10)

frame_lista.pack(fill="both", expand=True)
frame_entradas.pack(fill="x")
frame_botones.pack(fill="x")

# Crear tabla (TreeView) para mostrar los eventos
tree = ttk.Treeview(frame_lista, columns=("fecha", "hora", "desc"), show="headings")
tree.heading("fecha", text="Fecha")
tree.heading("hora", text="Hora")
tree.heading("desc", text="Descripción")

# Ajustar tamaños de columnas
tree.column("fecha", width=120, anchor="center")
tree.column("hora", width=80, anchor="center")
tree.column("desc", width=400, anchor="w")
tree.pack(fill="both", expand=True)

# Etiquetas y campos de entrada
ttk.Label(frame_entradas, text="Fecha:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entrada_fecha = DateEntry(frame_entradas, date_pattern="yyyy-mm-dd")
entrada_fecha.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame_entradas, text="Hora (HH:MM):").grid(row=0, column=2, padx=5, pady=5, sticky="w")
entrada_hora = ttk.Entry(frame_entradas, width=10)
entrada_hora.grid(row=0, column=3, padx=5, pady=5)

ttk.Label(frame_entradas, text="Descripción:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entrada_desc = ttk.Entry(frame_entradas, width=60)
entrada_desc.grid(row=1, column=1, columnspan=3, padx=5, pady=5)


# Función para agregar eventos a la tabla
def agregar_evento():
    fecha = entrada_fecha.get()
    hora = entrada_hora.get().strip()
    desc = entrada_desc.get().strip()

    if not hora or not desc:
        messagebox.showwarning("Campos vacíos", "Complete hora y descripción")
        return

    tree.insert("", "end", values=(fecha, hora, desc))

    # Limpiar campos después de agregar
    entrada_hora.delete(0, tk.END)
    entrada_desc.delete(0, tk.END)


# Función para eliminar evento seleccionado
def eliminar_evento():
    sel = tree.selection()
    if not sel:
        messagebox.showinfo("Eliminar", "Seleccione un evento")
        return

    if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar el evento seleccionado?"):
        for item in sel:
            tree.delete(item)


# Botones de acción
ttk.Button(frame_botones, text="Agregar Evento", command=agregar_evento).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Eliminar Evento", command=eliminar_evento).pack(side="left", padx=5)
ttk.Button(frame_botones, text="Salir", command=ventana.destroy).pack(side="right", padx=5)

# Ejecutar la aplicación
ventana.mainloop()
