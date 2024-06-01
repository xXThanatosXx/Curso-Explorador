# Guía de Tkinter

Esta guía proporciona los comandos necesarios para crear ventanas, botones, sliders, multiventanas, agregar imágenes y personalizar interfaces con Tkinter. Cada sección incluye un ejemplo en Python.

## Instalación

Para utilizar Tkinter, debes tener Python instalado. Tkinter viene incluido con Python.

## Crear una Ventana

Para crear una ventana básica con Tkinter:

```python
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Básica")

# Cambiar el tamaño de la ventana (ancho x alto)
ventana.geometry("800x600")  # Cambia estos valores según el tamaño deseado

# Ejecutar la ventana
ventana.mainloop()
```

### Función para salir de la ventana
```
def salir():
    ventana.destroy()
```

## Botones
Para crear un botón y agregarlo a la ventana:


```python

import tkinter as tk

def saludar():
    print("Hola, mundo")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Botón")

# Crear un botón
boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

# Ejecutar la ventana
ventana.mainloop()

```
## Crear Sliders

```python
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

```
## Crear Slider Vertical

```python

import tkinter as tk

def mostrar_valor(valor):
    print(f"Valor del slider: {valor}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Slider")

# Crear un slider
slider = tk.Scale(ventana, from_=0, to=100, orient='vertical', command=mostrar_valor)
slider.pack()

# Ejecutar la ventana
ventana.mainloop()
```
## Crear Multiventanas
```python
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

```

## Agregar Imágenes
```python
import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con Imagen")

# Cargar la imagen
imagen = Image.open("ruta/a/tu/imagen.png")
imagen_tk = ImageTk.PhotoImage(imagen)

# Crear una etiqueta con la imagen
etiqueta = tk.Label(ventana, image=imagen_tk)
etiqueta.pack()

# Ejecutar la ventana
ventana.mainloop()
```
## Personalizar Interfaces
```python
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Personalizada")
ventana.geometry("300x200")  # Tamaño de la ventana

# Personalizar el fondo
ventana.configure(bg="lightblue")

# Crear un botón personalizado
boton = tk.Button(ventana, text="Botón Personalizado", fg="white", bg="blue", font=("Arial", 14))
boton.pack(pady=20)

# Ejecutar la ventana
ventana.mainloop()

```
###
Recursos Adicionales

```python
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana Básica")

# Cambiar el tamaño de la ventana (ancho x alto)
ventana.geometry("800x600")  # Cambia estos valores según el tamaño deseado

# Variable para almacenar el valor
valor_almacenado = tk.IntVar()

# Función para almacenar el valor 0
def almacenar_cero():
    valor_almacenado.set(0)
    print(f"Valor almacenado: {valor_almacenado.get()}")

# Función para salir de la aplicación
def salir():
    ventana.destroy()

# Crear un botón para almacenar el valor 0
boton_almacenar = tk.Button(ventana, text="Almacenar 0", command=almacenar_cero)
boton_almacenar.pack(pady=20)  # Puedes ajustar 'pady' para la separación vertical

# Crear un botón para salir
boton_salir = tk.Button(ventana, text="Salir", command=salir)
boton_salir.pack(pady=20)  # Puedes ajustar 'pady' para la separación vertical

# Ejecutar la ventana
ventana.mainloop()
```