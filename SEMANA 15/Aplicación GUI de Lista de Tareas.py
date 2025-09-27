import tkinter as tk
from tkinter import messagebox

# Clase principal de la app
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        # Campo de entrada para escribir nuevas tareas
        self.entry = tk.Entry(root, width=35)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # Permite añadir con Enter

        # Botones de control
        frame_buttons = tk.Frame(root)
        frame_buttons.pack(pady=5)

        self.btn_add = tk.Button(frame_buttons, text="Añadir Tarea", width=15, command=self.add_task)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_complete = tk.Button(frame_buttons, text="Marcar como Completada", width=20, command=self.complete_task)
        self.btn_complete.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(frame_buttons, text="Eliminar Tarea", width=15, command=self.delete_task)
        self.btn_delete.grid(row=0, column=2, padx=5)

        # Listbox para mostrar las tareas
        self.listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.listbox.pack(pady=10)

        # Evento opcional: doble clic para marcar como completada
        self.listbox.bind("<Double-1>", self.complete_task)

    # Funciones de la aplicación

    def add_task(self, event=None):
        """Agrega una nueva tarea al Listbox."""
        task = self.entry.get().strip()
        if task != "":
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self, event=None):
        """Marca la tarea seleccionada como completada (agrega prefijo ✔)."""
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if not task.startswith("✔ "):  # Evitar marcar varias veces
                self.listbox.delete(index)
                self.listbox.insert(index, "✔ " + task)
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para completarla.")

    def delete_task(self):
        """Elimina la tarea seleccionada del Listbox."""
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Debes seleccionar una tarea para eliminarla.")

# Ejecución de la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
