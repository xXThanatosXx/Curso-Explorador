class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo de instancia
        self.edad = edad  # Atributo de instancia

    def saludar(self):  # Método de instancia
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 30)
persona1.saludar()  # Salida: Hola, me llamo Juan y tengo 30 años.


class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # Llamada al constructor de la clase base
        self.carrera = carrera  # Nuevo atributo para la clase derivada

    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}.")

# Crear un objeto de la clase Estudiante
estudiante1 = Estudiante("Ana", 22, "Ingeniería")
estudiante1.saludar()  # Salida: Hola, me llamo Ana y tengo 22 años.
estudiante1.estudiar()  # Salida: Ana está estudiando Ingeniería.
