#Leer un número entero de tres dígitos y determinar si el primer dígito es igual al último.

numInt=int(input("Ingrese un número de 3 dígitos"))

if(numInt>99 and numInt<1000):
    dig1=numInt//100
    dig2=(numInt%100)//10
    dig3= (numInt%100)%10

    if(dig1==dig3):
        print("El primer dígito es igual al último")
    else:
        print("El primer dígito no es igual al último")    
