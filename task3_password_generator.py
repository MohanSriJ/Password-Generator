import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Password", "Password length should be at least 4")
            return

        chars = ""
        if var_upper.get():
            chars += string.ascii_uppercase
        if var_lower.get():
            chars += string.ascii_lowercase
        if var_digits.get():
            chars += string.digits
        if var_symbols.get():
            chars += string.punctuation

        if not chars:
            messagebox.showerror("Error", "Select at least one character set!")
            return

        password = "".join(random.choice(chars) for _ in range(length))
        result_var.set(password)
    except:
        messagebox.showerror("Error", "Please enter a valid length")

# Function to copy password
def copy_password():
    pwd = result_var.get()
    if pwd:
        root.clipboard_clear()
        root.clipboard_append(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("No Password", "Generate a password first")

# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x400")
root.config(bg="black")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 20, "bold"), 
         bg="black", fg="white").pack(pady=10)

# Length Entry
tk.Label(root, text="Password Length:", font=("Arial", 14), bg="black", fg="white").pack()
length_entry = tk.Entry(root, font=("Arial", 14), justify="center")
length_entry.pack(pady=5)

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase", variable=var_upper, font=("Arial", 12),
               bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Lowercase", variable=var_lower, font=("Arial", 12),
               bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Digits", variable=var_digits, font=("Arial", 12),
               bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=60)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols, font=("Arial", 12),
               bg="black", fg="white", selectcolor="black").pack(anchor="w", padx=60)

# Result Display
result_var = tk.StringVar()
tk.Entry(root, textvariable=result_var, font=("Arial", 16, "bold"), 
         bg="white", fg="black", justify="center").pack(pady=10, ipadx=5, ipady=5)

# Buttons
btn_font = ("Arial", 14, "bold")
tk.Button(root, text="Generate", command=generate_password, font=btn_font, 
          bg="#FF9500", fg="white", relief="flat", width=12).pack(pady=5)
tk.Button(root, text="Copy", command=copy_password, font=btn_font, 
          bg="#A6A6A6", fg="black", relief="flat", width=12).pack(pady=5)

root.mainloop()
