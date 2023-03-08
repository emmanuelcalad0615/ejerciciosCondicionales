#Leer un número entero de tres dígitos y determinar si alguno de sus dígitos es igual a la suma de los otros dos.

numInt=int(input("Ingrese un número entero de tres dígitos"))

if(numInt>99 and numInt<1000):
    dig1=numInt//100
    dig2=(numInt%100)//10
    dig3=(numInt%100)%10

    suma1=dig1+dig2
    suma2=dig1+dig3
    suma3=dig2+dig3

    if(dig1==suma3):
        print(f"La suma entre el dígito 2 ({dig2}) y el dígto 3({dig3}) es igual al dígito 1({dig1})")
    elif(dig2==suma2):
        print(f"La suma entre el dígito 1 ({dig1}) y el dígto 3({dig3}) es igual al dígito 1({dig2})")
    elif(dig3==suma1):
        print(f"La suma entre el dígito 1 ({dig1}) y el dígto 2({dig2}) es igual al dígito 3({dig3})")    
    else:
        print("Ninguno de los dígitos es igual a la suma de los otros dos dígitos")    
