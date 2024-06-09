## Creación de ejecutable 

- pip install pyinstaller
- pyinstaller --onefile main.py

### modificadores
* (--onefile, --windowed y --icon=./nombre de icono.ico)

### función operaciones (operaciones)
```python
def suma(n1,n2):
    return n1+n2
def resta(n1,n2):
    return n1-n2

def multiplicacion(n1,n2):
    return n1*n2
def division(n1,n2):
    try:
        return n1/n2
    except ZeroDivisionError:
        print("no se puede dividir por cero")
        
```

### función principal main.py
```python
# from Calculadora import suma
import Operaciones as op

res = op.division(1,2)
print(res)

while(True):
    try:
        opc1 = float(input("Numero uno: "))
        opc2 = float(input("Numero dos: "))
        break
    except ValueError:
        print("debes ingresar un numero: ")

operacion = input("Introduce la operacion a realizar (suma,resta,multiplicacion, division)")

operacion.lower()

if operacion == "suma":
    print(op.suma(opc1,opc2))
elif operacion == "resta":
    print(op.resta(opc1,opc2))
elif operacion == "multiplicacion":
    print(op.multiplicacion(opc1,opc2))
elif operacion == "division":
    print(op.division(opc1,opc2))
else:
    print("Operacion no completada")

print("Programa Finalizado")
input("presiona enter para salir")


```