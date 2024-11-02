print("Adivine el numero secreto")
nombre = input("Digite su nombre: ")
apellidos = input("Digite sus apellidos: ")
edad = input("Digite su edad: ")

print("Bienvenido", nombre, apellidos)
numero =int(input("Digite un numero: "))

if 18 == numero: 
    print("Felicidades", nombre, apellidos,"ha adivinado el numero secreto: 18")
else:
    print("Gracias por su participacion")