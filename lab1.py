"""
nombre:calculadora
entrada:operacion,op1,op2
salida:resultado de la operación
restricciones:debe de ser entero,tiene que ser positivo
"""
def calculadora(operacion,op1,op2):
    if not isinstance(operacion,int):
        return "Error:debe de ser entero"
    if operacion<=0:
        return "Error:tiene que ser positivo"
    if not isinstance(op1,int):
        return "Error:debe de ser entero"
    if op1<=0:
        return "Error:tiene que ser positivo"
    if not isinstance(op2,int):
        return "Error:debe de ser entero"
    if op2<=0:
        return "Error:tiene que ser positivo"
    suma=1
    resta=2
    multiplicacion=3
    division=4
    if operacion==1:
        return(op1+op2)
    
    elif operacion==2:
         return(op1-op2)

    elif operacion==3:
         return(op1*op2)
     
    elif operacion==4:
     if op2==0:
        return "Error:No se puede dividir entre 0"
    else:
       return(op1//op2)

    if operacion>4:
        return "Error:la operacion no es valida"


"""
Nombre:contadorDigitos
entrada:numeros,digito
salida:numero de veces que el numero aparece en el numero
Restricciones:debe de ser entero,tiene que ser positivo
"""
def contadorDigitos(num,digito):
    if not isinstance(num,int):
        return "Error:el numero tiene que ser entero"
    if not isinstance(digito,int):
        return "Error:el numero tiene que ser entero"
    elif num<0:
        return "Error:el numero tiene que ser positivo"
    elif digito<0:
        return "Error:el numero tiene que ser positivo"
    else:
        return contadorDigitos_aux(num,digito)
def contadorDigitos_aux(num,digito):
    resultado=0
    i=0
    while num==digito:
     resultado=num%10
     resultado=digito+i
    return resultado
         

