import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

tasks = []

def add_task():
    task = task_entry.get()
    category = category_entry.get()
    if task and category:
        tasks.append({"task": task, "completed": False, "subtasks": [], "category": category})
        update_task_list()
        task_entry.delete(0, tk.END)
        category_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Lütfen bir görev ve kategori girin.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks):
        status = "Tamamlandı" if task["completed"] else "Tamamlanmadı"
        task_text = f"{idx + 1}. {task['task']}  ({task['category']}) - {status}"
        task_listbox.insert(tk.END, task_text)
        color = "green" if task["completed"] else "red"
        task_listbox.itemconfig(idx, {'bg': color})

def update_subtask_list(index):
    subtask_listbox.delete(0, tk.END)
    for subidx, subtask in enumerate(tasks[index]["subtasks"]):
        status = "Tamamlandı" if subtask["completed"] else "Tamamlanmadı"
        subtask_text = f"{subidx + 1}. {subtask['task']} - {status}"
        subtask_listbox.insert(tk.END, subtask_text)
        color = "green" if subtask["completed"] else "red"
        subtask_listbox.itemconfig(subidx, {'bg': color})

def complete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["completed"] = True
        update_task_list()
    except IndexError:
        messagebox.showerror("Hata", "Lütfen tamamlanacak bir görev seçin.")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        update_task_list()
        subtask_listbox.delete(0, tk.END)
    except IndexError:
        messagebox.showerror("Hata", "Lütfen silinecek bir görev seçin.")

def edit_task():
    try:
        index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        new_category = category_entry.get("")
        if new_task and new_category:
            tasks[index]["task"] = new_task
            tasks[index]["category"] = new_category
            update_task_list()
            task_entry.delete(0, tk.END)
            category_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Uyarı", "Lütfen yeni bir görev ve kategori girin.")
    except IndexError:
        messagebox.showerror("Hata", "Lütfen düzenlenecek bir görev seçin.")

def add_subtask():
    try:
        index = task_listbox.curselection()[0]
        subtask = subtask_entry.get()
        if subtask:
            tasks[index]["subtasks"].append({"task": subtask, "completed": False})
            update_subtask_list(index)
            subtask_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Uyarı", "Lütfen bir alt görev girin.")
    except IndexError:
        messagebox.showerror("Hata", "Lütfen alt görev eklemek için bir ana görev seçin.")

def complete_subtask():
    try:
        task_index = task_listbox.curselection()[0]
        subtask_index = subtask_listbox.curselection()[0]
        tasks[task_index]["subtasks"][subtask_index]["completed"] = True
        update_subtask_list(task_index)
    except IndexError:
        messagebox.showerror("Hata", "Lütfen tamamlanacak bir alt görev seçin.")

def delete_subtask():
    try:
        task_index = task_listbox.curselection()[0]
        subtask_index = subtask_listbox.curselection()[0]
        tasks[task_index]["subtasks"].pop(subtask_index)
        update_subtask_list(task_index)
    except IndexError:
        messagebox.showerror("Hata", "Lütfen silinecek bir alt görev seçin.")

root = tk.Tk()
root.title("To-Do List Uygulaması")

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

category_entry = tk.Entry(root, width=50)
category_entry.pack(pady=10)

add_button = tk.Button(root, text="Görev Ekle", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

complete_button = tk.Button(root, text="Görevi Tamamla", command=complete_task)
complete_button.pack(pady=5)

delete_button = tk.Button(root, text="Görev Sil", command=delete_task)
delete_button.pack(pady=5)

edit_button = tk.Button(root, text="Görevi Düzenle", command=edit_task)
edit_button.pack(pady=5)

subtask_listbox = tk.Listbox(root, width=50, height=10)
subtask_listbox.pack(pady=10)

subtask_entry = tk.Entry(root, width=50)
subtask_entry.pack(pady=10)

add_subtask_button = tk.Button(root, text="Alt Görev Ekle", command=add_subtask)
add_subtask_button.pack(pady=5)

complete_subtask_button = tk.Button(root, text="Alt Görevi Tamamla", command=complete_subtask)
complete_subtask_button.pack(pady=5)

delete_subtask_button = tk.Button(root, text="Alt Görevi Sil", command=delete_subtask)
delete_subtask_button.pack(pady=5)

def on_task_select(event):
    try:
        index = task_listbox.curselection()[0]
        update_subtask_list(index)
    except IndexError:
        pass

task_listbox.bind("<<ListboxSelect>>", on_task_select)
root.mainloop()
