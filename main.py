import tkinter as tk
from tkinter import filedialog, messagebox

def modify_value(entry, change):
    try:
        current_value = int(entry.get())
        new_value = current_value + change
        entry.delete(0, tk.END)
        entry.insert(0, str(new_value))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(0, "8000")
def reset_life_points(p_entry1, p_entry2, p_entry_path):
    p_entry1.delete(0,tk.END)
    p_entry1.insert(0, "8000")
    p_entry2.delete(0,tk.END)
    p_entry2.insert(0, "8000")
    save_input_to_file(p_entry1, "player1.txt", p_entry_path)
    save_input_to_file(p_entry2, "player2.txt", p_entry_path)
def save_input_to_file(entry, filename, path_entry):
    directory = path_entry.get()
    if not directory:
        messagebox.showerror("Error", "Please specify the directory path.")
        return
    filepath = f"{directory}/{filename}"
    try:
        with open(filepath, 'w') as file:
            file.write(entry.get())
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file. {e}")

def create_app():
    root = tk.Tk()
    root.title("Life Points Calculator for OBS")

    root.grid_columnconfigure(1, minsize=200)

    root.configure(bg='#333333')
    style_color = '#333333'
    button_color = '#E1E1E1'

    entry_path = tk.Entry(root, width=60)
    entry_path.insert(0, "C:\\Users\\BOUBOU\\Documents\\YGO_OBS")
    entry_path.grid(row=0, column=2, columnspan=6)

    label_path = tk.Label(root, text="Directory Path where the files are saved:")
    label_path.grid(row=0, column=0, columnspan=1)
    label_path.configure(bg='#333333', fg="#FFFFFF")
    entry1 = tk.Entry(root, width=20)
    entry1.insert(0, "8000")
    entry1.grid(row=1, column=0)

    modify_buttons1 = [
        ("+1000", 1000), ("-1000", -1000), 
        ("+100", 100), ("-100", -100)
    ]
    for i, (label, value) in enumerate(modify_buttons1, start=1):
        button = tk.Button(root, text=label, command=lambda v=value, e=entry1: modify_value(e, v))
        button.grid(row=1, column=i)

    button_save1 = tk.Button(root, text="Save Player 1", command=lambda: save_input_to_file(entry1, "player1.txt", entry_path))
    button_save1.grid(row=1, column=5)

    entry2 = tk.Entry(root, width=20)
    entry2.insert(0, "8000")
    entry2.grid(row=2, column=0)

    modify_buttons2 = [
        ("+1000", 1000), ("-1000", -1000), 
        ("+100", 100), ("-100", -100)
    ]
    for i, (label, value) in enumerate(modify_buttons2, start=1):
        button = tk.Button(root, text=label, command=lambda v=value, e=entry2: modify_value(e, v))
        button.grid(row=2, column=i)

    button_save2 = tk.Button(root, text="Save Player 2", command=lambda: save_input_to_file(entry2, "player2.txt", entry_path))
    button_save2.grid(row=2, column=5)

    button_reset = tk.Button(root, text="Reset Life Points", command=lambda: reset_life_points(entry1, entry2, entry_path))
    button_reset.grid(row=3, column=0)

    root.mainloop()

if __name__ == "__main__":
    create_app()
