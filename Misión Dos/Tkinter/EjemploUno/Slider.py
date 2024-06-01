import tkinter as tk

def mostrar_valor(valor):
    print(f"Valor del slider: {valor}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Slider")

# Crear un slider
slider = tk.Scale(ventana, from_=0, to=100, orient='horizontal', command=mostrar_valor)
slider.pack()

# Ejecutar la ventana
ventana.mainloop()