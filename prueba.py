def suma(valor,total):
    return valor+total

def resta(valor,total):
    return valor-total

def producto(valor,total):
    return valor*total

def division(valor,total):
    return total/valor

def calculadora():
    opc=0
    valor=0
    valor1=0
    total=0
    valor=float(input("Ingrese número 1: "))
    while(opc==0):
        
        opc=input("Ingrese operación ")
        valor1=float(input("Ingrese número 2: "))
        ter=str(input("Ingrese = si desea terminar o 0 si desea continuar: "))
        if(opc=='+'):
            if(ter=='='):
                print (suma(valor,valor1))
                opc=1
            else:
                valor = suma(valor,valor1)
                opc=0
        if(opc=='-'):
            if(ter=='='):
                print(resta(valor,valor1))
                opc=1
            else:
                valor=resta(valor,valor1)
                opc=0
        if(opc=='*'):
            if(ter=='='):
                print(producto(valor,valor1))
                opc=1
            else:
                valor=producto(valor,valor1)
                opc=0
        if(opc=='/'):
            if(ter=='='):
                print(division(valor1,valor))
                opc=1
            else:
                valor=division(valor1,valor)
                opc=0

calculadora()