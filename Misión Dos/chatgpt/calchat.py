import tkinter as tk
from tkinter import messagebox

def obtener_numeros():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        return n1, n2
    except ValueError:
        messagebox.showerror("Error", "Debe introducir números válidos")
        return None, None

def sumar():
    n1, n2 = obtener_numeros()
    if n1 is not None and n2 is not None:
        resultado.set(f"La suma es: {n1 + n2}")

def restar():
    n1, n2 = obtener_numeros()
    if n1 is not None and n2 is not None:
        resultado.set(f"La resta es: {n1 - n2}")

def multiplicar():
    n1, n2 = obtener_numeros()
    if n1 is not None and n2 is not None:
        resultado.set(f"La multiplicación es: {n1 * n2}")

def dividir():
    n1, n2 = obtener_numeros()
    if n1 is not None and n2 is not None:
        try:
            resultado.set(f"La división es: {n1 / n2}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "No se puede dividir por cero")

def limpiar():
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    resultado.set("")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Variables
resultado = tk.StringVar()

# Interfaz de usuario
frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Ingrese el primer número:").grid(row=0, column=0, padx=10, pady=5)
entry_n1 = tk.Entry(frame)
entry_n1.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Ingrese el segundo número:").grid(row=1, column=0, padx=10, pady=5)
entry_n2 = tk.Entry(frame)
entry_n2.grid(row=1, column=1, padx=10, pady=5)

tk.Button(frame, text="Sumar", command=sumar).grid(row=2, column=0, padx=10, pady=5)
tk.Button(frame, text="Restar", command=restar).grid(row=2, column=1, padx=10, pady=5)
tk.Button(frame, text="Multiplicar", command=multiplicar).grid(row=3, column=0, padx=10, pady=5)
tk.Button(frame, text="Dividir", command=dividir).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, textvariable=resultado, font=('Helvetica', 12)).pack(pady=20)
tk.Button(root, text="Limpiar", command=limpiar).pack()

# Ejecución del bucle principal
root.mainloop()
