print("Bienvenido, digite la cantidad de examenes y sus calificaciones, en caso de no contar con uno, digite 0")

num1 = int(input("Digite el numero de examenes realizados: "))
num2 = int(input("Digite la calificacion del primer examen: "))
num3 = int(input("Digite la calificacion del segundo examen: "))
num4 = int(input("Digite la calificacion del tercer examen: "))
num5 = int(input("Digite la calificacion del cuarto examen: "))
num6 = int(input("Digite la calificacion del quinto examen: "))

suma = num2+num3+num4+num5+num6
promedio = suma/num1

print("Su promedio es de:",promedio)

if promedio>=70:
    print("Usted ha aprobado el curso")
    
if promedio==60<=69:
    print("Usted debe realizar ampliacion")

if promedio<60:
    print("Usted ha desaprobado el curso")
