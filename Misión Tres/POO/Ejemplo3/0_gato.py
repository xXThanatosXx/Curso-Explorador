class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo del gato
        self.edad = edad      # Atributo del gato

    def maullar(self):
        return f"{self.nombre} está maullando!"

    def es_mayor_que(self, otro_gato):
        return self.edad > otro_gato.edad

# Crear objetos de la clase Gato
gato1 = Gato("Pelusa", 3)
gato2 = Gato("Bigotes", 5)

# Llamar a métodos de los objetos
print(gato1.maullar())  # Pelusa está maullando!
print(f"¿Pelusa es mayor que Bigotes? {'Sí' if gato1.es_mayor_que(gato2) else 'No'}")
