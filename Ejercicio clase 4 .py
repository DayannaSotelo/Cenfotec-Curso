#Se desea saber si el numero ingresado por el usuario es mayor a 100, si el numero solicitado es mayor debera mostrar el numero -100 y si es menor a 100 debe de mostrar el 0, no se podra utilizar numeros menores a 0, en caso contrario debe de notificar el error existente

num = int(input("Digite un número: "))
if num>100:
    num = num - 100
    print ("El numero", num, "es mayor a 100")
    
if num >= 0:
    print ("El numero", num, "es menor que 100")
else:
    print ("El numero digitado no puede ser igual o menor a 0")