#5. Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.

numInt=int(input("Ingrese un número entero de dos dígitos: "))

if(numInt>9 and numInt<100):
    dig1=numInt//10
    dig2=numInt%10
    if(dig1>dig2):
        if(dig1%dig2==0):
            print(f"{dig1} es multiplo de {dig2}")
        else:
            print(f"{dig1} no es multiplo de {dig2}")    
    elif(dig2>dig1):
        if(dig2%dig1==0):
            print(f"{dig1} es multiplo de {dig2}")
        else:
            print(f"{dig1} no es multiplo de {dig2}")
    else:
        if(dig1%dig2==0):
            print(f"{dig1} es multiplo de {dig2}")
        else:
            print(f"{dig1} no es multiplo de {dig2}") 
               
                


else:
    print("Ingrese un número de dos dígitos")