import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Personalizada")
ventana.geometry("300x200")  # Tamaño de la ventana

# Personalizar el fondo
ventana.configure(bg="lightblue")

# Crear un botón personalizado
boton = tk.Button(ventana, text="Botón Personalizado", fg="black", bg="yellow", font=("Arial", 14))
boton.pack(pady=40)


# Ejecutar la ventana
ventana.mainloop()
