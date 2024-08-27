# Ejemplo Gato

### Definición de la clase Gato: 
Se crea la clase Gato con dos atributos (nombre y edad) y dos métodos (maullar y es_mayor_que).
### Constructor __init__: 
Este método especial se llama automáticamente cada vez que se crea un nuevo objeto de esa clase. Inicializa los atributos del objeto con los valores proporcionados.
### Creación de objetos gato1 y gato2: 
Se crean dos instancias de la clase Gato.
### Uso de métodos: 

maullar() es llamado en gato1, y es_mayor_que() compara las edades de gato1 y gato2.

### Encapsulamiento
El encapsulamiento es el principio de ocultar los detalles internos del funcionamiento de una clase y exponer solo los componentes necesarios para el resto del programa. Esto se logra mediante el uso de métodos públicos (que pueden ser accedidos desde fuera de la clase) y atributos o métodos privados (que están ocultos y solo pueden ser accedidos dentro de la clase).

### Protección o Control de Acceso
En Python, la protección de atributos y métodos se maneja principalmente a través de convenciones, utilizando un guion bajo (_) para atributos protegidos y doble guion bajo (__) para atributos privados.

- Atributos protegidos (_): son para uso interno de la clase y sus subclases.
- Atributos privados (__): son accesibles solo dentro de la clase donde se definen.

### El polimorfismo:
Es la capacidad de utilizar una interfaz común para diferentes tipos de datos o clases. En POO, permite que métodos con el mismo nombre actúen de manera diferente en función de los objetos con los que interactúan.

### Herencia:
La herencia permite la reutilización de código y en la organización jerárquica de las clases. La herencia permite que una clase (llamada subclase o clase derivada) herede atributos y métodos de otra clase (llamada superclase o clase base).

#### Ventajas de la Herencia
-Reutilización de Código: Permite reutilizar código de las clases base, lo que reduce la duplicación de código.
-Organización Lógica: Facilita la organización lógica de clases en jerarquías y promueve la claridad en el diseño del programa.
-Extensibilidad: Hace que el software sea más extensible ya que las nuevas funcionalidades pueden ser creadas partiendo de las ya existentes.

Clase Animal: Es la clase base que tiene un constructor para inicializar el nombre del animal y un método sonido() que es general para todos los animales.
Clases Gato y Perro: Son subclases de Animal y heredan sus atributos y métodos. Ambas clases sobrescriben el método sonido() para proporcionar un comportamiento específico para cada tipo de animal.

#### Tipos de Herencia
Herencia Simple: Una clase deriva de una sola clase base.
Herencia Múltiple: Una clase puede heredar de más de una clase base. Python soporta herencia múltiple, lo que permite combinar atributos y métodos de varias clases base.

- Uso de super(): En la herencia, a menudo es necesario llamar a un método de la clase base desde la clase derivada. Python proporciona la función super() para permitir esto.

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llama al constructor de la clase base
        self.raza = raza          # Nuevo atributo para Gato

mi_gato = Gato("Pelusa", "Siames")
print(f"{mi_gato.nombre} es un {mi_gato.raza}")

```