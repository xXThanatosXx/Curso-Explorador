# Ejercicio Práctico de POO: Sistema de Gestión de una Biblioteca

El objetivo de este ejercicio es implementar un sistema simplificado de gestión de una biblioteca utilizando los conceptos de POO en Python, como herencia, encapsulamiento, y polimorfismo.

Descripción del Sistema
El sistema debe ser capaz de gestionar libros y revistas, registrar préstamos y devoluciones, y mantener un registro de los diferentes tipos de materiales disponibles en la biblioteca.

Paso 1: Crear la Clase Base
Define una clase base llamada MaterialBibliografico que contenga atributos comunes y métodos que serán heredados por las subclases Libro y Revista.

```python
class MaterialBibliografico:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def info(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.año_publicacion}"

```

Paso 2: Crear Subclases para Libros y Revistas
Define las subclases Libro y Revista que heredan de MaterialBibliografico. Añade atributos y métodos específicos para cada tipo de material.

<!-- ```python
class Libro(MaterialBibliografico):
    def __init__(self, titulo, autor, año_publicacion, isbn):
        super().__init__(titulo, autor, año_publicacion)
        self.isbn = isbn

    def info(self):
        return f"{super().info()}, ISBN: {self.isbn}"

class Revista(MaterialBibliografico):
    def __init__(self, titulo, autor, año_publicacion, numero):
        super().__init__(titulo, autor, año_publicacion)
        self.numero = numero

    def info(self):
        return f"{super().info()}, Número: {self.numero}"

```
 -->
Paso 3: Implementar Funcionalidades de Préstamo y Devolución
Define una clase GestorPrestamos que maneje los préstamos y las devoluciones de los materiales bibliográficos.
<!-- ```python
class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def prestar_material(self, material, usuario):
        self.prestamos.append((material, usuario))
        print(f"{material.titulo} ha sido prestado a {usuario}.")

    def devolver_material(self, material, usuario):
        self.prestamos.remove((material, usuario))
        print(f"{material.titulo} ha sido devuelto por {usuario}.")

``` -->

Paso 4: Prueba el Sistema
Crea instancias de Libro y Revista, realiza algunos préstamos y devoluciones, y muestra la información de los materiales.

<!-- ```python
libro1 = Libro("1984", "George Orwell", 1949, "1234567890")
revista1 = Revista("National Geographic", "Varios autores", 2020, 102)

gestor = GestorPrestamos()
gestor.prestar_material(libro1, "Juan Pérez")
gestor.devolver_material(libro1, "Juan Pérez")

print(libro1.info())
print(revista1.info())
``` -->
