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


# import tkinter as tk


# def saludar():
#      print("Hola, mundo")
# # Crear la ventana principal
# ventana = tk.Tk()
# ventana.title("Ventana con Distintos Padding")

# # Crear un botón con padding vertical
# boton1 = tk.Button(ventana, text="Saludar",command=saludar)
# boton1.pack(pady=20)

# # Crear un botón con padding horizontal
# boton2 = tk.Button(ventana, text="Botón 2 (padx=20)")
# boton2.pack(padx=20)

# # Crear un botón con padding interno vertical
# boton3 = tk.Button(ventana, text="Botón 3 (ipady=10)")
# boton3.pack(ipady=10)

# # Crear un botón con padding interno horizontal
# boton4 = tk.Button(ventana, text="Botón 4 (ipadx=10)")
# boton4.pack(ipadx=10)

# # Ejecutar la ventana
# ventana.mainloop()
