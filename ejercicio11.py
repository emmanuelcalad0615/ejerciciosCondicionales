#. Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
numInt= int(input("Ingrese un número de tres dígitos: "))



if(numInt>99 and numInt<1000):
    dig1=numInt//100
    dig2=(numInt%100)//10
    dig3=(numInt%10)%10
    if(dig1!= dig2 and dig2!=dig3):
        if(dig1>dig2 and dig1>dig3):
            print(f"El dígito mayor {dig1} está ubicado en la posición 1")
        elif(dig2>dig1 and dig2>dig3):
            print(f"El dígito mayor {dig2} está ubicado en la posición 2")
        elif(dig3>dig2 and dig3>dig1):
            print(f"El dígito mayor {dig3} está ubicado en la posición 3")     
        else:
            print("Todos los dígitos son iguales")   
    elif(dig1!=dig2 and dig1==dig3):
        if(dig1>dig2 and dig1>dig3):
            print(f"El dígito mayor {dig1} está ubicado en la posición 1")
        elif(dig2>dig1 and dig2>dig3):
            print(f"El dígito mayor {dig2} está ubicado en la posición 2")
        elif(dig3>dig2 and dig3>dig1):
            print(f"El dígito mayor {dig3} está ubicado en la posición 3")     
        else:
            print("Todos los dígitos son iguales")  
    elif(dig1==dig2 and dig1!=dig3):
        if(dig1>dig2 and dig1>dig3):
            print(f"El dígito mayor {dig1} está ubicado en la posición 1")
        elif(dig2>dig1 and dig2>dig3):
            print(f"El dígito mayor {dig2} está ubicado en la posición 2")
        elif(dig3>dig2 and dig3>dig1):
            print(f"El dígito mayor {dig3} está ubicado en la posición 3")     
        else:
            print("Todos los dígitos son iguales")  
    elif(dig2!=dig1 and dig2==dig3):
        if(dig1>dig2 and dig1>dig3):
            print(f"El dígito mayor {dig1} está ubicado en la posición 1")
        elif(dig2>dig1 and dig2>dig3):
            print(f"El dígito mayor {dig2} está ubicado en la posición 2")
        elif(dig3>dig2 and dig3>dig1):
            print(f"El dígito mayor {dig3} está ubicado en la posición 3")     
        else:
            print("Todos los dígitos son iguales")   
    else:
        print("Todos los digitos son iguales")               




else:
    print("El número ingresado no es de 3 dígitos")    