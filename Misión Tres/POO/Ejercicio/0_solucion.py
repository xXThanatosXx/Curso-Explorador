class MaterialBibliografico:
    def __init__(self, titulo, autor, año_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion

    def info(self):
        return f"{self.titulo} por {self.autor}, publicado en {self.año_publicacion}"

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

class GestorPrestamos:
    def __init__(self):
        self.prestamos = []

    def prestar_material(self, material, usuario):
        self.prestamos.append((material, usuario))
        print(f"{material.titulo} ha sido prestado a {usuario}.")

    def devolver_material(self, material, usuario):
        self.prestamos.remove((material, usuario))
        print(f"{material.titulo} ha sido devuelto por {usuario}.")

libro1 = Libro("1984", "George Orwell", 1949, "1234567890")
revista1 = Revista("National Geographic", "Varios autores", 2020, 102)

gestor = GestorPrestamos()
gestor.prestar_material(libro1, "Juan Pérez")
gestor.devolver_material(libro1, "Juan Pérez")

print(libro1.info())
print(revista1.info())
