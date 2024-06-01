import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Básica")

# Cambiar el tamaño de la ventana (ancho x alto)
ventana.geometry("800x600")  # Cambia estos valores según el tamaño deseado

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=20)  # Puedes ajustar 'pady' para la separación vertical

# Ejecutar la ventana
ventana.mainloop()

