class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.raza = raza          # Nuevo atributo para Gato

mi_gato = Gato("Pelusa", "Siames")
print(f"{mi_gato.nombre} es un {mi_gato.raza}")


