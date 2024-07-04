# Author: Michael Brost
# Version 1.0
# Created on 2024-07-04
# Please gamble responsible!

import tkinter as tk
from tkinter import messagebox
import random

def generate_eurojackpot_fields(num_fields=14, main_numbers_range=50, euro_numbers_range=12):
    # Generate main numbers
    main_numbers = list(range(1, main_numbers_range + 1))
    random.shuffle(main_numbers)
    
    # Generate euro numbers
    euro_numbers = list(range(1, euro_numbers_range + 1))
    random.shuffle(euro_numbers)
    
    # Ensure each field has 5 main numbers and 2 euro numbers
    fields = []
    for _ in range(num_fields):
        field_main_numbers = random.sample(main_numbers, 5)
        field_euro_numbers = random.sample(euro_numbers, 2)
        fields.append((sorted(field_main_numbers), sorted(field_euro_numbers)))
    
    return fields

def generate_fields(event=None):
    try:
        num_fields = int(entry.get())
        if num_fields > 14:
            messagebox.showerror("Error", "Only up to 14 fields can be generated.")
        else:
            eurojackpot_fields = generate_eurojackpot_fields(num_fields=num_fields)
            result_text = ""
            for idx, field in enumerate(eurojackpot_fields):
                result_text += f"Field {idx + 1}: Main numbers: {field[0]}, Euro numbers: {field[1]}\n\n"
            result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Eurojackpot Field Generator")

# Set size of window
root.geometry("600x775")

# Set fonts
label_font = ("Helvetica", 18)
entry_font = ("Helvetica", 18)
button_font = ("Helvetica", 18, "bold")
result_font = ("Helvetica", 18)

# Create and place the widgets
tk.Label(root, text="Number of fields to generate (maximum 14):", font=label_font).pack(pady=10)
entry = tk.Entry(root, font=entry_font)
entry.pack(pady=5)
entry.focus_set()  # Set focus to the entry field

generate_button = tk.Button(root, text="Generate fields", command=generate_fields, font=button_font)
generate_button.pack(pady=20)

result_label = tk.Label(root, text="", justify=tk.LEFT, font=result_font)
result_label.pack(pady=10, padx=20)  # Increase horizontal padding with padx and vertical padding with pady

# Bind the Enter key to the generate_fields function
root.bind('<Return>', generate_fields)

# Start the main event loop
root.mainloop()
