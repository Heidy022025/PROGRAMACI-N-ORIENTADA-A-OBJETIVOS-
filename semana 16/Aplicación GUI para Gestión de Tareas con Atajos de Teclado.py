import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")

        # Campo de entrada
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(pady=10, padx=10, fill="x")
        self.entry.focus()

        # Botones
        btn_frame = tk.Frame(root, bg="#f0f0f0")
        btn_frame.pack(pady=5)

        self.add_btn = tk.Button(btn_frame, text="Añadir", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(btn_frame, text="Completar", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(btn_frame, text="Eliminar", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(padx=10, pady=10, fill="both", expand=True)

        # Atajos de teclado
        root.bind("<Return>", lambda event: self.add_task())
        root.bind("<c>", lambda event: self.complete_task())
        root.bind("<C>", lambda event: self.complete_task())
        root.bind("<d>", lambda event: self.delete_task())
        root.bind("<D>", lambda event: self.delete_task())
        root.bind("<Delete>", lambda event: self.delete_task())
        root.bind("<Escape>", lambda event: self.close_app)

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task = self.task_listbox.get(index)

            if not task.startswith("[✔]"):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"[✔] {task}")
            else:
                messagebox.showinfo("Info", "La tarea ya está completada.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

    def close_app(self, event=None):
        self.root.quit()

# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
