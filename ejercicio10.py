#Leer un número entero de tres dígitos y determinar si al menos dos de sus tres dígitos son iguales.

numInt=int(input("Ingrese un número entero de tres dígitos: "))
if(numInt>99 and numInt<1000):
    dig1= numInt//100
    dig2= (numInt%100)//10
    dig3= (numInt%10)%10

    if(dig1==dig2 or dig1==dig3 or dig2==dig3):
        print("El número tiene dígitos en común")
    else:
        print("El número no tiene dígitos en común")    



else:
    print("El número entero no es de tres dígitos")    