# herencia
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def sonido(self):
        return "Este animal hace un sonido"

class Gato(Animal):
    def sonido(self):
        return "Maulla"

class Perro(Animal):
    def sonido(self):
        return "Ladra"

# Creación de instancias de Gato y Perro
mi_gato = Gato("Pelusa")
mi_perro = Perro("Rex")

print(mi_gato.sonido())  # Maulla
print(mi_perro.sonido())  # Ladra
