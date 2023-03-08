#Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros.

numInt=int(input("Ingrese un número entero de tres dígitos"))


dig1=numInt//100
dig2=(numInt%100)//10
dig3=(numInt%100)%10
res=dig1%dig2
print(f"{res}")
print(f"{dig1}{dig2}{dig3}")

if(dig1%dig2==0 or dig2%dig1==0 or dig3%dig1==0 or dig1%dig3==0 or dig3%dig2==0 or dig2%dig3==0):
    print("Existen dígitos multiplos  de otros en el número ingresado")
else:
    print("No hay dígitos multiplos de otros en el número ingresado")    
