#Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales

numInt=int(input("Ingrese un número entero de dos dígitos: "))
if(numInt<10 or numInt>99):
    print("El número ingresado no es de 2 dígitos")
    
else:
    dig1=numInt%10
    dig2=numInt//10
    if(dig1== dig2):
        print("Los dígitos ingresados son iguales")
    else:
        print("Los dígitos ingresados no son iguales")    