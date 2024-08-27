class Gato:
    def __init__(self, nombre, edad):
        self.nombre = nombre      # Atributo público
        self.__edad = edad        # Atributo privado (encapsulado)
        self.dueño = None         # Referencia al dueño del gato

    def asignar_dueño(self, dueño):
        self.dueño = dueño

    def mostrar_info(self):
        info = f"{self.nombre} tiene {self.__edad} años."
        if self.dueño:
            info += f" Su dueño es {self.dueño.nombre}."
        return info


class Dueño:
    def __init__(self, nombre):
        self.nombre = nombre      # Atributo público
        self.gatos = []           # Lista de gatos que posee el dueño

    def adoptar_gato(self, gato):
        self.gatos.append(gato)
        gato.asignar_dueño(self)

    def mostrar_gatos(self):
        info = f"{self.nombre} tiene los siguientes gatos:\n"
        for gato in self.gatos:
            info += f"- {gato.nombre}\n"
        return info


# Crear objetos de las clases
gato1 = Gato("Luna", 4)
gato2 = Gato("Salem", 3)
dueño1 = Dueño("Alice")

# Establecer relaciones
dueño1.adoptar_gato(gato1)
dueño1.adoptar_gato(gato2)

# Mostrar información
print(gato1.mostrar_info())  # Luna tiene 4 años. Su dueño es Alice.
print(gato2.mostrar_info())  # Salem tiene 3 años. Su dueño es Alice.
print(dueño1.mostrar_gatos())  
# Alice tiene los siguientes gatos:
# - Luna
# - Salem
