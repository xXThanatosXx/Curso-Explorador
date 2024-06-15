import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Imagen")

# Cargar la imagen
ruta_imagen = "D:/Shadow/GitHub/Curso-Explorador/Misión Tres/Tkinter/EjemploUno/Cat.jpg"
imagen = Image.open(ruta_imagen)

# Redimensionar la imagen
nuevo_ancho, nuevo_alto = 200, 200  # Tamaño deseado
imagen = imagen.resize((nuevo_ancho, nuevo_alto), Image.Resampling.LANCZOS)

# Convertir la imagen redimensionada a un objeto ImageTk.PhotoImage
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear una etiqueta con la imagen
etiqueta = tk.Label(ventana, image=imagen_tk)
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()
