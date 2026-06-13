import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        value = float(value_entry.get())
        choice = option.get()

        if choice == "KM to Miles":
            result = value * 0.621371

        elif choice == "Celsius to Fahrenheit":
            result = (value * 9/5) + 32

        elif choice == "KG to Pounds":
            result = value * 2.20462

        result_label.config(
            text=f"Result: {round(result, 2)}"
        )

    except:
        messagebox.showerror(
            "Error",
            "Enter valid number"
        )

def clear():
    value_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here")

window = tk.Tk()
window.title("Unit Converter")
window.geometry("400x300")

title = tk.Label(
    window,
    text="Unit Converter",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

value_entry = tk.Entry(window, width=25)
value_entry.pack(pady=10)

option = tk.StringVar()
option.set("KM to Miles")

menu = tk.OptionMenu(
    window,
    option,
    "KM to Miles",
    "Celsius to Fahrenheit",
    "KG to Pounds"
)
menu.pack(pady=10)

tk.Button(
    window,
    text="Convert",
    command=convert,
    width=20
).pack(pady=5)

tk.Button(
    window,
    text="Clear",
    command=clear,
    width=20
).pack(pady=5)

result_label = tk.Label(
    window,
    text="Result will appear here",
    font=("Arial", 12)
)
result_label.pack(pady=15)

window.mainloop()