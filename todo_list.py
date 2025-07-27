import tkinter as tk
from tkinter import messagebox

tasks = []

# Function Definitions

def add_task():
    task = entry.get()
    if task:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(checkbox_frame, text=task, variable=var, font=("Calibri", 11), bg="#96f7b0", anchor="w", width=30)
        checkbox.var = var
        checkbox.pack(anchor='w')
        tasks.append((task, checkbox))
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "You forgot to type something!")

def remove_task():
    try:
        selected = listbox.curselection()[0]
        task_text = listbox.get(selected)
        for t in tasks:
            if t[0] == task_text:
                t[1].destroy()  # destroy checkbox
                tasks.remove(t)
                break
        update_listbox()
    except IndexError:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

def clear_all():
    confirm = messagebox.askyesno("Clear All", "Are you sure you want to delete all tasks?")
    if confirm:
        for t in tasks:
            t[1].destroy()  # destroy checkbox
        tasks.clear()
        update_listbox()

def save_tasks():
    with open("tasks.txt", "w") as file:
        for t in tasks:
            file.write(t[0] + "\n")
    messagebox.showinfo("Saved!", "Your tasks were saved successfully!")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                task = line.strip()
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(checkbox_frame, text=task, variable=var, font=("Calibri", 11), bg="#96f7b0", anchor="w", width=30)
                checkbox.var = var
                checkbox.pack(anchor='w')
                tasks.append((task, checkbox))
        update_listbox()
    except FileNotFoundError:
        pass

def update_listbox():
    listbox.delete(0, tk.END)
    for t in tasks:
        listbox.insert(tk.END, t[0])

# GUI Setup

root = tk.Tk()
root.title("🌟 Task Tracker")
root.geometry("450x500")
root.config(bg="#96f7b0")

# Entry

entry = tk.Entry(root, font=("Calibri", 12), width=30)
entry.grid(row=0, column=0, padx=10, pady=10)

add_btn = tk.Button(root, text="➕ Add", width=12, bg="#7cd8f1", command=add_task)
add_btn.grid(row=0, column=1, padx=5)

# Listbox

listbox = tk.Listbox(root, font=("Helvetica", 11), width=40, height=6, selectbackground="#d57bc6")
listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=(0,5))

# Checkbox area

checkbox_frame = tk.Frame(root, bg="#96f7b0")
checkbox_frame.grid(row=2, column=0, columnspan=2, pady=5)

# Buttons

del_btn = tk.Button(root, text="🗑️ Delete Selected", width=20, bg="#f4adf8", command=remove_task)
del_btn.grid(row=3, column=0, columnspan=2, pady=5)

clear_btn = tk.Button(root, text="🧹 Clear All", width=20, bg="#c5d0f7", command=clear_all)
clear_btn.grid(row=4, column=0, columnspan=2, pady=5)

save_btn = tk.Button(root, text="💾 Save Tasks", width=20, bg="#d5e8d4", command=save_tasks)
save_btn.grid(row=5, column=0, columnspan=2, pady=5)

# Load tasks on startup
load_tasks()

# Start GUI loop
root.mainloop()
