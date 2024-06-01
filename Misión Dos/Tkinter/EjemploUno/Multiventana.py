import tkinter as tk

def abrir_nueva_ventana():
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.title("Nueva Ventana")
    etiqueta = tk.Label(nueva_ventana, text="Esto es una nueva ventana")
    etiqueta.pack()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Principal")

# Crear un botón para abrir una nueva ventana
boton = tk.Button(ventana, text="Abrir Nueva Ventana", command=abrir_nueva_ventana)
boton.pack()

# Ejecutar la ventana
ventana.mainloop()