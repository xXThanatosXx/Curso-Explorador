import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de Valores")
ventana.geometry("300x200")

# Variable para almacenar la suma
suma = tk.IntVar()
suma.set(0)

# Función para sumar los valores de los botones
def sumar_valor(valor):
    suma.set(suma.get() + valor)
    etiqueta_resultado.config(text=f"Suma: {suma.get()}")

# Crear los botones con sus valores
boton1 = tk.Button(ventana, text="Botón 1 (Valor 1)", command=lambda: sumar_valor(1))
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Botón 2 (Valor 2)", command=lambda: sumar_valor(2))
boton2.pack(pady=10)

# Crear una etiqueta para mostrar la suma
etiqueta_resultado = tk.Label(ventana, text="Suma: 0", font=("Arial", 16))
etiqueta_resultado.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()
