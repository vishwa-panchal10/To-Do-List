import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📝 To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        self.tasks = []

        # --- Title ---
        tk.Label(root, text="My To-Do List", font=("Helvetica", 20, "bold")).pack(pady=20)

        # --- Entry for new tasks ---
        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=25)
        self.task_entry.pack(pady=10)

        # --- Buttons ---
        add_btn = tk.Button(root, text="Add Task", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=self.add_task)
        add_btn.pack(pady=5)

        delete_btn = tk.Button(root, text="Delete Selected Task", font=("Helvetica", 12), bg="#f44336", fg="white", command=self.delete_task)
        delete_btn.pack(pady=5)

        clear_btn = tk.Button(root, text="Clear All Tasks", font=("Helvetica", 12), bg="#FF9800", fg="white", command=self.clear_tasks)
        clear_btn.pack(pady=5)

        # --- Task listbox ---
        self.listbox = tk.Listbox(root, font=("Helvetica", 14), width=40, height=15)
        self.listbox.pack(pady=20)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            selected_index = self.listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def clear_tasks(self):
        self.tasks.clear()
        self.update_listbox()

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
