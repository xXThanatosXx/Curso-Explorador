# Polimorfismo

class Gato:
    def sonido(self):
        return "Maullido"

class Perro:
    def sonido(self):
        return "Ladrido"

def escuchar_animal(animal):
    print(animal.sonido())

# Polimorfismo en acción
mi_gato = Gato()
mi_perro = Perro()
escuchar_animal(mi_gato)  # Maullido
escuchar_animal(mi_perro)  # Ladrido
