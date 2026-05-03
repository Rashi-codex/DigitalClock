import tkinter as tk
from datetime import datetime 
from tkinter import ttk
root = tk.Tk()
root.title("Digital Clock")
root.geometry("500x400")
root.configure(bg="black")
def update_clock() -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_clock)
label=ttk.Label(root, font=("Helvetica", 48), background="black", foreground="white")
label.pack(expand=True)
update_clock()
def reset_clock():
    label.config(text="00:00:00")

button = ttk.Button(root, text="Reset Clock", command=reset_clock, style="TButton")
button.pack(pady=20)
root.mainloop()