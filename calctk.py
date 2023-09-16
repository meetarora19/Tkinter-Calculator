import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(background="grey")

        self.entry = tk.Entry(root, font=("Arial", 18), justify="right", bd=0, relief="flat", bg="black", fg="blue")
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10, sticky="we")

        buttons = [
            ("sin", 1, 0), ("log", 1, 1), ("(", 1, 2), (")", 1, 3), ("x!", 1, 4),
            ("cos", 2, 0), ("C", 2, 1), ("%", 2, 2), ("⌫", 2, 3), ("÷", 2, 4),
            ("tan", 3, 0), ("7", 3, 1), ("8", 3, 2), ("9", 3, 3), ("x", 3, 4),
            ("xʸ", 4, 0), ("4", 4, 1), ("5", 4, 2), ("6", 4, 3), ("-", 4, 4),
            ("√", 5, 0), ("1", 5, 1), ("2", 5, 2), ("3", 5, 3), ("+", 5, 4),
            ("", 6, 0), ("00", 6, 1), ("0", 6, 2), (".", 6, 3), ("=", 6, 4)
        ]

        for button in buttons:
            text, row, column = button
            button = tk.Button(root, text=text, font=("Arial", 16, "bold"), width=5, height=2, bd=0, relief="flat",
                           command=lambda text=text: self.handle_button_click(text))
            button.grid(row=row, column=column, padx=5, pady=5, sticky="we")
            button.configure(bg="black", fg="blue", activebackground="black", activeforeground="white",
                             highlightbackground="pink", highlightthickness=0)
            button.bind("<Enter>", lambda event, btn=button: btn.config(bg="blue", fg="black"))
            button.bind("<Leave>", lambda event, btn=button: btn.config(bg="black", fg="blue"))

    def handle_button_click(self, text):
        if text == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "sin":
            try:
                num = float(self.entry.get())
                result = math.sin(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "cos":
            try:
                num = float(self.entry.get())
                result = math.cos(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "tan":
            try:
                num = float(self.entry.get())
                result = math.tan(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "C":
            self.entry.delete(0, tk.END)
        elif text == "x":
            self.entry.insert(tk.END, "*")
        elif text == "÷":
            self.entry.insert(tk.END, "/")
        elif text == "√":
            try:
                num = float(self.entry.get())
                result = num ** 0.5
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "xʸ":
            try:
                num = float(self.entry.get())
                power = float(tk.simpledialog.askstring("Power", "Enter the power:"))
                result = num ** power
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "⌫":  
            current_expression = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_expression[:-1])
        elif text == "log":
            try:
                num = float(self.entry.get())
                result = math.log10(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        elif text == "(":
            self.entry.insert(tk.END, "(")
        elif text == ")":
            self.entry.insert(tk.END, ")")
        elif text == "x!":
            try:
                num = int(self.entry.get())
                result = math.factorial(num)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            self.entry.insert(tk.END, text)
root = tk.Tk()
root.configure(background="#E0E0E0")
root.geometry("400x500")
root.resizable(False, False)
root.title("Calculator")

calculator = Calculator(root)
root.wm_attributes("-transparentcolor", 'grey')
root.mainloop()
