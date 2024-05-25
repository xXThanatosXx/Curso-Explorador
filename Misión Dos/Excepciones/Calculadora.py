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
        


