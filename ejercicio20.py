#Leer un número entero de cinco dígitos y determinar si es un número capicúa. Ej. 15651,59895.

numInt=int(input("Ingrese un número de 5 dígitos"))
if(numInt>9999 and numInt<100000):
    dig1=numInt//10000
    dig2=(numInt%10000)//1000
    dig3=(numInt%1000)//100
    dig4=(numInt%100)//10
    dig5=numInt%10
    
    derecho=f"{dig1}{dig2}{dig3}{dig4}{dig5}"
    reves=f"{dig5}{dig4}{dig3}{dig2}{dig1}"

    if(derecho==reves):
        print("El número es un número capicúa")
    else:
        print("El número no es un número capicúa")    