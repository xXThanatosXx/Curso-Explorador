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


