# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:20:18 2025

@author: Hp
"""

import re
import tkinter as tk

# List of common weak passwords
weak_passwords = ["123456", "password", "12345678", "qwerty", "abc123", "password1", "12345"]

# Function to check password strength
def check_password_strength():
    password = password_entry.get()  # Get the entered password
    
    # Check length
    if len(password) < 8:
        result_label.config(text="Weak: Password must be at least 8 characters long.", fg="red")
        return
    
    # Check for uppercase, lowercase, digit, and special character
    if not re.search(r"[A-Z]", password):
        result_label.config(text="Weak: Password must include at least one uppercase letter.", fg="red")
        return
    if not re.search(r"[a-z]", password):
        result_label.config(text="Weak: Password must include at least one lowercase letter.", fg="red")
        return
    if not re.search(r"[0-9]", password):
        result_label.config(text="Weak: Password must include at least one number.", fg="red")
        return
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result_label.config(text="Weak: Password must include at least one special character.", fg="red")
        return

    # Check against common passwords
    if password in weak_passwords:
        result_label.config(text="Weak: This password is too common. Choose a more unique one.", fg="red")
        return

    # If all conditions are met
    result_label.config(text="Strong: Your password is secure!", fg="green")

# Function to clear input and result
def clear_input():
    password_entry.delete(0, tk.END)
    result_label.config(text="", fg="black")

# Create the GUI application
app = tk.Tk()
app.title("Password Strength Checker")
app.geometry("400x200")

# Label for instructions
instruction_label = tk.Label(app, text="Enter a password to check its strength:", font=("Arial", 12))
instruction_label.pack(pady=10)

# Input field for password
password_entry = tk.Entry(app, show="*", width=30, font=("Arial", 12))
password_entry.pack(pady=5)

# Button to check strength
check_button = tk.Button(app, text="Check Strength", command=check_password_strength, bg="blue", fg="white", font=("Arial", 10))
check_button.pack(pady=10)

# Label to display results
result_label = tk.Label(app, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Clear button
clear_button = tk.Button(app, text="Clear", command=clear_input, bg="gray", fg="white", font=("Arial", 10))
clear_button.pack(pady=5)

# Run the application
app.mainloop()
